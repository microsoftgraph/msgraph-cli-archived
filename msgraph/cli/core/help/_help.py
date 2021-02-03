# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

# This file is extracted from azure-cli with changes made to make it work for msgraph-cli

from __future__ import print_function
import argparse

from msgraph.cli.core.commands import ExtensionCommandSource
from knack.help import (HelpFile as KnackHelpFile, CommandHelpFile as KnackCommandHelpFile,
                        GroupHelpFile as KnackGroupHelpFile, HelpExample as KnackHelpExample,
                        HelpParameter as KnackHelpParameter, _print_indent, CLIHelp,
                        HelpAuthoringException)
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)

FIRST_LINE_PREFIX = ' : '
REQUIRED_TAG = '[Required]'
LINE_FORMAT = u'{cli}{name}{separator}{summary}'


def _get_line_len(name, tags_len):
    return len(name) + tags_len + (2 if tags_len else 1)


def _get_hanging_indent(max_length, indent):
    return max_length + (indent * 4) + len(FIRST_LINE_PREFIX) - 1


def _get_padding_len(max_len, layout):
    if layout['tags']:
        pad_len = max_len - layout['line_len'] + 1
    else:
        pad_len = max_len - layout['line_len']
    return pad_len


class ArgumentGroupRegistry(object):  # pylint: disable=too-few-public-methods
    def __init__(self, group_list):

        self.priorities = {
            None: 0,
            'Global Arguments': 1000,
        }
        priority = 2
        # any groups not already in the static dictionary should be prioritized alphabetically
        other_groups = [g for g in sorted(list(set(group_list))) if g not in self.priorities]
        for group in other_groups:
            self.priorities[group] = priority
            priority += 1

    def get_group_priority(self, group_name):
        key = self.priorities.get(group_name, 0)
        return "%06d" % key


PRIVACY_STATEMENT = """
Welcome to Microsoft Graph CLI!
---------------------
Use `mg -h` to see available commands or go to https://aka.ms/microsoftgraph.

Telemetry
---------
The Microsoft Graph CLI collects usage data in order to improve your experience.
The data is anonymous and does not include commandline argument values.
The data is collected by Microsoft.

You can change your telemetry settings with `mg configure`.
"""

WELCOME_MESSAGE = r'''

___  ____                           __ _     _____                 _
|  \/  (_)                         / _| |   |  __ \               | |
| .  . |_  ___ _ __ ___  ___  ___ | |_| |_  | |  \/_ __ __ _ _ __ | |__
| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __| | | __| '__/ _` | '_ \| '_ \
| |  | | | (__| | | (_) \__ \ (_) | | | |_  | |_\ \ | | (_| | |_) | | | |
\_|  |_/_|\___|_|  \___/|___/\___/|_|  \__|  \____/_|  \__,_| .__/|_| |_|
                                                            | |
                                                            |_|

Welcome to the Microsoft Graph CLI!

Use mg --version to display the current version
Here are the base commands
'''

# PrintMixin class to decouple printing functionality from GraphCliHelp class.
# Most of these methods override print methods in CLIHelp.


class CLIPrintMixin(CLIHelp):
    def _print_header(self, cli_name, help_file):
        super(CLIPrintMixin, self)._print_header(cli_name, help_file)

        links = help_file.links
        if links:
            link_text = "{} and {}".format(", ".join([link["url"] for link in links[0:-1]]),
                                           links[-1]["url"]) if len(links) > 1 else links[0]["url"]
            link_text = "For more information, see: {}\n".format(link_text)
            _print_indent(link_text, 2, width=self.textwrap_width)

    def _print_detailed_help(self, cli_name, help_file):
        CLIPrintMixin._print_extensions_msg(help_file)
        super(CLIPrintMixin, self)._print_detailed_help(cli_name, help_file)
        self._print_mg_find_message(help_file.command, self.cli_ctx.enable_color)

    @staticmethod
    def _get_choices_defaults_sources_str(p):
        choice_str = '  Allowed values: {}.'.format(', '.join(sorted([str(x) for x in p.choices]))) \
            if p.choices else ''
        default_value_source = p.default_value_source if p.default_value_source else 'Default'
        default_str = '  {}: {}.'.format(default_value_source, p.default) \
            if p.default and p.default != argparse.SUPPRESS else ''
        value_sources_str = CLIPrintMixin._process_value_sources(p) if p.value_sources else ''
        return '{}{}{}'.format(choice_str, default_str, value_sources_str)

    @staticmethod
    def _print_examples(help_file):
        indent = 0
        _print_indent('Examples', indent)
        for e in help_file.examples:
            indent = 1
            _print_indent('{0}'.format(e.short_summary), indent)
            indent = 2
            if e.long_summary:
                _print_indent('{0}'.format(e.long_summary), indent)
            _print_indent('{0}'.format(e.command), indent)
            print('')

    @staticmethod
    def _print_mg_find_message(command, enable_color):
        from colorama import Style
        indent = 0
        message = 'For more specific examples, use: mg find "mg {}"'.format(command)
        if enable_color:
            message = Style.BRIGHT + message + Style.RESET_ALL
        _print_indent(message + '\n', indent)

    @staticmethod
    def _process_value_sources(p):
        commands, strings, urls = [], [], []

        for item in p.value_sources:
            if "string" in item:
                strings.append(item["string"])
            elif "link" in item and "command" in item["link"]:
                commands.append(item["link"]["command"])
            elif "link" in item and "url" in item["link"]:
                urls.append(item["link"]["url"])

        command_str = '  Values from: {}.'.format(", ".join(commands)) if commands else ''
        string_str = '  {}'.format(", ".join(strings)) if strings else ''
        string_str = string_str + "." if string_str and not string_str.endswith(".") else string_str
        urls_str = '  For more info, go to: {}.'.format(", ".join(urls)) if urls else ''
        return '{}{}{}'.format(command_str, string_str, urls_str)

    @staticmethod
    def _print_extensions_msg(help_file):
        if help_file.type != 'command':
            return
        if isinstance(help_file.command_source, ExtensionCommandSource):
            logger.warning(help_file.command_source.get_command_warn_msg())

            # Extension preview/experimental warning is disabled because it can be confusing when displayed together
            # with command or command group preview/experimental warning. See #12556

            # # If experimental is true, it overrides preview
            # if help_file.command_source.experimental:
            #     logger.warning(help_file.command_source.get_experimental_warn_msg())
            # elif help_file.command_source.preview:
            #     logger.warning(help_file.command_source.get_preview_warn_msg())


class GraphCliHelp(CLIPrintMixin, CLIHelp):
    def __init__(self, cli_ctx):
        super(GraphCliHelp, self).__init__(cli_ctx,
                                           privacy_statement=PRIVACY_STATEMENT,
                                           welcome_message=WELCOME_MESSAGE,
                                           command_help_cls=CliCommandHelpFile,
                                           group_help_cls=CliGroupHelpFile,
                                           help_cls=CliHelpFile)
        from knack.help import HelpObject

        # TODO: This workaround is used to avoid a bizarre bug in Python 2.7. It
        # essentially reassigns Knack's HelpObject._normalize_text implementation
        # with an identical implemenation in Az. For whatever reason, this fixes
        # the bug in Python 2.7.
        @staticmethod
        def new_normalize_text(s):
            if not s or len(s) < 2:
                return s or ''
            s = s.strip()
            initial_upper = s[0].upper() + s[1:]
            trailing_period = '' if s[-1] in '.!?' else '.'
            return initial_upper + trailing_period

        HelpObject._normalize_text = new_normalize_text  # pylint: disable=protected-access

        self._register_help_loaders()
        self._name_to_content = {}

    def show_help(self, cli_name, nouns, parser, is_group):
        self.update_loaders_with_help_file_contents(nouns)

        delimiters = ' '.join(nouns)
        help_file = self.command_help_cls(self, delimiters, parser) if not is_group \
            else self.group_help_cls(self, delimiters, parser)
        help_file.load(parser)
        if not nouns:
            help_file.command = ''
        else:
            GraphCliHelp.update_examples(help_file)

        self._print_detailed_help(cli_name, help_file)
        # TODO: Show updates available
        show_link = self.cli_ctx.config.getboolean('output', 'show_survey_link', True)

        # TODO: Show survey prompts
        if show_link:
            pass

    def _register_help_loaders(self):
        import msgraph.cli.core.help._help_loaders as help_loaders
        import inspect

        def is_loader_cls(cls):
            return inspect.isclass(cls) and cls.__name__ != 'BaseHelpLoader' and issubclass(cls, help_loaders.BaseHelpLoader)  # pylint: disable=line-too-long

        versioned_loaders = {}
        for cls_name, loader_cls in inspect.getmembers(help_loaders, is_loader_cls):
            loader = loader_cls(self)
            versioned_loaders[cls_name] = loader

        if len(versioned_loaders) != len({ldr.version for ldr in versioned_loaders.values()}):
            ldrs_str = " ".join("{}-version:{}".format(cls_name, ldr.version) for cls_name, ldr in versioned_loaders.items())  # pylint: disable=line-too-long
            raise CLIError("Two loaders have the same version. Loaders:\n\t{}".format(ldrs_str))

        self.versioned_loaders = versioned_loaders

    def update_loaders_with_help_file_contents(self, nouns):
        loader_file_names_dict = {}
        file_name_set = set()
        for ldr_cls_name, loader in self.versioned_loaders.items():
            new_file_names = loader.get_noun_help_file_names(nouns) or []
            loader_file_names_dict[ldr_cls_name] = new_file_names
            file_name_set.update(new_file_names)

        for file_name in file_name_set:
            if file_name not in self._name_to_content:
                with open(file_name, 'r') as f:
                    self._name_to_content[file_name] = f.read()

        for ldr_cls_name, file_names in loader_file_names_dict.items():
            file_contents = {}
            for name in file_names:
                file_contents[name] = self._name_to_content[name]
            self.versioned_loaders[ldr_cls_name].update_file_contents(file_contents)

    # This method is meant to be a hook that can be overridden by an extension or module.
    @staticmethod
    def update_examples(help_file):
        pass

    def _print_arguments(self, help_file):  # pylint: disable=too-many-statements

        LINE_FORMAT = u'{name}{padding}{tags}{separator}{short_summary}'
        indent = 1
        self.max_line_len = 0

        if not help_file.parameters:
            _print_indent('None', indent)
            _print_indent('')
            return None

        def _build_tags_string(item):

            preview_info = getattr(item, 'preview_info', None)
            preview = preview_info.tag if preview_info else ''

            experimental_info = getattr(item, 'experimental_info', None)
            experimental = experimental_info.tag if experimental_info else ''

            deprecate_info = getattr(item, 'deprecate_info', None)
            deprecated = deprecate_info.tag if deprecate_info else ''

            required = REQUIRED_TAG if getattr(item, 'required', None) else ''
            tags = ' '.join(
                [x
                 for x in [str(deprecated),
                           str(preview), str(experimental), required] if x])
            tags_len = sum(
                [len(deprecated),
                 len(preview),
                 len(experimental),
                 len(required),
                 tags.count(' ')])
            if not tags_len:
                tags = ''
            return tags, tags_len

        def _layout_items(items):

            layouts = []
            for c in sorted(items, key=_get_parameter_key):

                deprecate_info = getattr(c, 'deprecate_info', None)
                if deprecate_info and not deprecate_info.show_in_help():
                    continue

                tags, tags_len = _build_tags_string(c)
                short_summary = _build_short_summary(c)
                long_summary = _build_long_summary(c)
                line_len = _get_line_len(c.name, tags_len)
                layout = {
                    'name': c.name,
                    'tags': tags,
                    'separator': FIRST_LINE_PREFIX if short_summary else '',
                    'short_summary': short_summary,
                    'long_summary': long_summary,
                    'group_name': c.group_name,
                    'line_len': line_len
                }
                if line_len > self.max_line_len:
                    self.max_line_len = line_len
                layouts.append(layout)
            return layouts

        def _print_items(layouts):
            last_group_name = ''

            for layout in layouts:
                indent = 1
                if layout['group_name'] != last_group_name:
                    if layout['group_name']:
                        print('')
                        print(layout['group_name'])
                    last_group_name = layout['group_name']

                layout['padding'] = ' ' * _get_padding_len(self.max_line_len, layout)
                _print_indent(
                    LINE_FORMAT.format(**layout),
                    indent,
                    _get_hanging_indent(self.max_line_len, indent),
                    width=self.textwrap_width,
                )

                indent = 2
                long_summary = layout.get('long_summary', None).split('\n')[0]
                if long_summary:
                    _print_indent(long_summary, indent, width=self.textwrap_width)

            _print_indent('')

        def _build_short_summary(item):
            short_summary = item.short_summary
            possible_values_index = short_summary.find(' Possible values include')
            short_summary = short_summary[
                0:possible_values_index if possible_values_index >= 0 else len(short_summary)]
            short_summary += self._get_choices_defaults_sources_str(item)
            short_summary = short_summary.strip()
            return short_summary

        def _build_long_summary(item):
            lines = []
            if item.long_summary:
                lines.append(item.long_summary)
            deprecate_info = getattr(item, 'deprecate_info', None)
            if deprecate_info:
                lines.append(str(item.deprecate_info.message))
            preview_info = getattr(item, 'preview_info', None)
            if preview_info:
                lines.append(str(item.preview_info.message))
            experimental_info = getattr(item, 'experimental_info', None)
            if experimental_info:
                lines.append(str(item.experimental_info.message))
            return ' '.join(lines)

        group_registry = ArgumentGroupRegistry(
            [p.group_name for p in help_file.parameters if p.group_name])

        def _get_parameter_key(parameter):
            return u'{}{}{}'.format(group_registry.get_group_priority(parameter.group_name),
                                    str(not parameter.required), parameter.name)

        parameter_layouts = _layout_items(help_file.parameters)
        _print_items(parameter_layouts)

        return indent


class CliHelpFile(KnackHelpFile):
    def __init__(self, help_ctx, delimiters):
        # Each help file (for a command or group) has a version denoting the source of its data.
        super(CliHelpFile, self).__init__(help_ctx, delimiters)
        self.links = []

    def _should_include_example(self, ex):
        supported_profiles = ex.get('supported-profiles')
        unsupported_profiles = ex.get('unsupported-profiles')

        if all((supported_profiles, unsupported_profiles)):
            raise HelpAuthoringException(
                "An example cannot have both supported-profiles and unsupported-profiles.")

        if supported_profiles:
            supported_profiles = [profile.strip() for profile in supported_profiles.split(',')]
            return self.help_ctx.cli_ctx.cloud.profile in supported_profiles

        if unsupported_profiles:
            unsupported_profiles = [profile.strip() for profile in unsupported_profiles.split(',')]
            return self.help_ctx.cli_ctx.cloud.profile not in unsupported_profiles

        return True

    # Needs to override base implementation to exclude unsupported examples.
    def _load_from_data(self, data):
        if not data:
            return

        if isinstance(data, str):
            self.long_summary = data
            return

        if 'type' in data:
            self.type = data['type']

        if 'short-summary' in data:
            self.short_summary = data['short-summary']

        self.long_summary = data.get('long-summary')

        if 'examples' in data:
            self.examples = []
            for d in data['examples']:
                if self._should_include_example(d):
                    self.examples.append(HelpExample(**d))

    def load(self, options):
        ordered_loaders = sorted(self.help_ctx.versioned_loaders.values(),
                                 key=lambda ldr: ldr.version)
        for loader in ordered_loaders:
            loader.versioned_load(self, options)


class CliGroupHelpFile(KnackGroupHelpFile, CliHelpFile):
    def load(self, options):
        # forces class to use this load method even if KnackGroupHelpFile overrides CliHelpFile's method.
        CliHelpFile.load(self, options)


class CliCommandHelpFile(KnackCommandHelpFile, CliHelpFile):
    def __init__(self, help_ctx, delimiters, parser):
        super(CliCommandHelpFile, self).__init__(help_ctx, delimiters, parser)
        self.type = 'command'
        self.command_source = getattr(parser, 'command_source', None)

        self.parameters = []

        for action in [a for a in parser._actions if a.help != argparse.SUPPRESS]:  # pylint: disable=protected-access
            if action.option_strings:
                self._add_parameter_help(action)
            else:
                # use metavar for positional parameters
                param_kwargs = {
                    'name_source': [action.metavar or action.dest],
                    'deprecate_info': getattr(action, 'deprecate_info', None),
                    'preview_info': getattr(action, 'preview_info', None),
                    'experimental_info': getattr(action, 'experimental_info', None),
                    'default_value_source': getattr(action, 'default_value_source', None),
                    'description': action.help,
                    'choices': action.choices,
                    'required': False,
                    'default': None,
                    'group_name': 'Positional'
                }
                self.parameters.append(HelpParameter(**param_kwargs))

        help_param = next(p for p in self.parameters if p.name == '--help -h')
        help_param.group_name = 'Global Arguments'

        # update parameter type so we can use overriden update_from_data method to update value sources.
        for param in self.parameters:
            param.__class__ = HelpParameter

    def _load_from_data(self, data):
        super(CliCommandHelpFile, self)._load_from_data(data)

        if isinstance(data, str) or not self.parameters or not data.get('parameters'):
            return

        loaded_params = []
        loaded_param = {}
        for param in self.parameters:
            loaded_param = next((n for n in data['parameters'] if n['name'] == param.name), None)
            if loaded_param:
                param.update_from_data(loaded_param)
            loaded_params.append(param)

        self.parameters = loaded_params

    def load(self, options):
        # forces class to use this load method even if KnackCommandHelpFile overrides CliHelpFile's method.
        CliHelpFile.load(self, options)


class HelpExample(KnackHelpExample):  # pylint: disable=too-few-public-methods
    def __init__(self, **_data):
        # Old attributes
        _data['name'] = _data.get('name', '')
        _data['text'] = _data.get('text', '')
        super(HelpExample, self).__init__(_data)

        self.name = _data.get('summary', '') if _data.get('summary', '') else self.name
        self.text = _data.get('command', '') if _data.get('command', '') else self.text

        self.long_summary = _data.get('description', '')
        self.supported_profiles = _data.get('supported-profiles', None)
        self.unsupported_profiles = _data.get('unsupported-profiles', None)

    # alias old params with new
    @property
    def short_summary(self):
        return self.name

    @short_summary.setter
    def short_summary(self, value):
        self.name = value

    @property
    def command(self):
        return self.text

    @command.setter
    def command(self, value):
        self.text = value


class HelpParameter(KnackHelpParameter):  # pylint: disable=too-many-instance-attributes
    def __init__(self, **kwargs):
        super(HelpParameter, self).__init__(**kwargs)

    def update_from_data(self, data):
        super(HelpParameter, self).update_from_data(data)
        # original help.py value_sources are strings, update command strings to value-source dict
        if self.value_sources:
            self.value_sources = [
                str_or_dict if isinstance(str_or_dict, dict) else {
                    "link": {
                        "command": str_or_dict
                    }
                } for str_or_dict in self.value_sources
            ]
