# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['mail_beta'] = '''
    type: group
    short-summary: Manage Mail
'''

helps['mail user'] = """
    type: group
    short-summary: Manage user with mail_beta
"""

helps['mail user create-mail-folder'] = """
    type: command
    short-summary: "Create new navigation property to mailFolders for users."
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail user create-message'] = """
    type: command
    short-summary: "Create new navigation property to messages for users."
"""

helps['mail user delete-inference-classification'] = """
    type: command
    short-summary: "Delete navigation property inferenceClassification for users."
"""

helps['mail user delete-mail-folder'] = """
    type: command
    short-summary: "Delete navigation property mailFolders for users."
"""

helps['mail user delete-message'] = """
    type: command
    short-summary: "Delete navigation property messages for users."
"""

helps['mail user list-mail-folder'] = """
    type: command
    short-summary: "Get mailFolders from users."
"""

helps['mail user list-message'] = """
    type: command
    short-summary: "Get messages from users."
"""

helps['mail user set-message-content'] = """
    type: command
    short-summary: "Update media content for the navigation property messages in users."
"""

helps['mail user show-inference-classification'] = """
    type: command
    short-summary: "Get inferenceClassification from users."
"""

helps['mail user show-mail-folder'] = """
    type: command
    short-summary: "Get mailFolders from users."
"""

helps['mail user show-message'] = """
    type: command
    short-summary: "Get messages from users."
"""

helps['mail user show-message-content'] = """
    type: command
    short-summary: "Get media content for the navigation property messages from users."
"""

helps['mail user update-inference-classification'] = """
    type: command
    short-summary: "Update the navigation property inferenceClassification in users."
"""

helps['mail user update-mail-folder'] = """
    type: command
    short-summary: "Update the navigation property mailFolders in users."
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail user update-message'] = """
    type: command
    short-summary: "Update the navigation property messages in users."
"""

helps['mail usersinferenceclassification'] = """
    type: group
    short-summary: Manage usersinferenceclassification with mail_beta
"""

helps['mail usersinferenceclassification create-override'] = """
    type: command
    short-summary: "Create new navigation property to overrides for users."
    parameters:
      - name: --sender-email-address
        short-summary: "emailAddress"
        long-summary: |
            Usage: --sender-email-address address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail usersinferenceclassification delete-override'] = """
    type: command
    short-summary: "Delete navigation property overrides for users."
"""

helps['mail usersinferenceclassification list-override'] = """
    type: command
    short-summary: "Get overrides from users."
"""

helps['mail usersinferenceclassification show-override'] = """
    type: command
    short-summary: "Get overrides from users."
"""

helps['mail usersinferenceclassification update-override'] = """
    type: command
    short-summary: "Update the navigation property overrides in users."
    parameters:
      - name: --sender-email-address
        short-summary: "emailAddress"
        long-summary: |
            Usage: --sender-email-address address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail usersmailfolder'] = """
    type: group
    short-summary: Manage usersmailfolder with mail_beta
"""

helps['mail usersmailfolder create-child-folder'] = """
    type: command
    short-summary: "Create new navigation property to childFolders for users."
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail usersmailfolder create-message'] = """
    type: command
    short-summary: "Create new navigation property to messages for users."
"""

helps['mail usersmailfolder create-message-rule'] = """
    type: command
    short-summary: "Create new navigation property to messageRules for users."
"""

helps['mail usersmailfolder create-multi-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to multiValueExtendedProperties for users."
"""

helps['mail usersmailfolder create-single-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to singleValueExtendedProperties for users."
"""

helps['mail usersmailfolder create-user-configuration'] = """
    type: command
    short-summary: "Create new navigation property to userConfigurations for users."
"""

helps['mail usersmailfolder delete-child-folder'] = """
    type: command
    short-summary: "Delete navigation property childFolders for users."
"""

helps['mail usersmailfolder delete-message'] = """
    type: command
    short-summary: "Delete navigation property messages for users."
"""

helps['mail usersmailfolder delete-message-rule'] = """
    type: command
    short-summary: "Delete navigation property messageRules for users."
"""

helps['mail usersmailfolder delete-multi-value-extended-property'] = """
    type: command
    short-summary: "Delete navigation property multiValueExtendedProperties for users."
"""

helps['mail usersmailfolder delete-single-value-extended-property'] = """
    type: command
    short-summary: "Delete navigation property singleValueExtendedProperties for users."
"""

helps['mail usersmailfolder delete-user-configuration'] = """
    type: command
    short-summary: "Delete navigation property userConfigurations for users."
"""

helps['mail usersmailfolder list-child-folder'] = """
    type: command
    short-summary: "Get childFolders from users."
"""

helps['mail usersmailfolder list-message'] = """
    type: command
    short-summary: "Get messages from users."
"""

helps['mail usersmailfolder list-message-rule'] = """
    type: command
    short-summary: "Get messageRules from users."
"""

helps['mail usersmailfolder list-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users."
"""

helps['mail usersmailfolder list-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users."
"""

helps['mail usersmailfolder list-user-configuration'] = """
    type: command
    short-summary: "Get userConfigurations from users."
"""

helps['mail usersmailfolder set-message-content'] = """
    type: command
    short-summary: "Update media content for the navigation property messages in users."
"""

helps['mail usersmailfolder show-child-folder'] = """
    type: command
    short-summary: "Get childFolders from users."
"""

helps['mail usersmailfolder show-message'] = """
    type: command
    short-summary: "Get messages from users."
"""

helps['mail usersmailfolder show-message-content'] = """
    type: command
    short-summary: "Get media content for the navigation property messages from users."
"""

helps['mail usersmailfolder show-message-rule'] = """
    type: command
    short-summary: "Get messageRules from users."
"""

helps['mail usersmailfolder show-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users."
"""

helps['mail usersmailfolder show-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users."
"""

helps['mail usersmailfolder show-user-configuration'] = """
    type: command
    short-summary: "Get userConfigurations from users."
"""

helps['mail usersmailfolder update-child-folder'] = """
    type: command
    short-summary: "Update the navigation property childFolders in users."
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail usersmailfolder update-message'] = """
    type: command
    short-summary: "Update the navigation property messages in users."
"""

helps['mail usersmailfolder update-message-rule'] = """
    type: command
    short-summary: "Update the navigation property messageRules in users."
"""

helps['mail usersmailfolder update-multi-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property multiValueExtendedProperties in users."
"""

helps['mail usersmailfolder update-single-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property singleValueExtendedProperties in users."
"""

helps['mail usersmailfolder update-user-configuration'] = """
    type: command
    short-summary: "Update the navigation property userConfigurations in users."
"""

helps['mail usersmailfoldersmessage'] = """
    type: group
    short-summary: Manage usersmailfoldersmessage with mail_beta
"""

helps['mail usersmailfoldersmessage create-attachment'] = """
    type: command
    short-summary: "Create new navigation property to attachments for users."
"""

helps['mail usersmailfoldersmessage create-extension'] = """
    type: command
    short-summary: "Create new navigation property to extensions for users."
"""

helps['mail usersmailfoldersmessage create-mention'] = """
    type: command
    short-summary: "Create new navigation property to mentions for users."
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail usersmailfoldersmessage create-multi-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to multiValueExtendedProperties for users."
"""

helps['mail usersmailfoldersmessage create-single-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to singleValueExtendedProperties for users."
"""

helps['mail usersmailfoldersmessage delete-attachment'] = """
    type: command
    short-summary: "Delete navigation property attachments for users."
"""

helps['mail usersmailfoldersmessage delete-extension'] = """
    type: command
    short-summary: "Delete navigation property extensions for users."
"""

helps['mail usersmailfoldersmessage delete-mention'] = """
    type: command
    short-summary: "Delete navigation property mentions for users."
"""

helps['mail usersmailfoldersmessage delete-multi-value-extended-property'] = """
    type: command
    short-summary: "Delete navigation property multiValueExtendedProperties for users."
"""

helps['mail usersmailfoldersmessage delete-single-value-extended-property'] = """
    type: command
    short-summary: "Delete navigation property singleValueExtendedProperties for users."
"""

helps['mail usersmailfoldersmessage list-attachment'] = """
    type: command
    short-summary: "Get attachments from users."
"""

helps['mail usersmailfoldersmessage list-extension'] = """
    type: command
    short-summary: "Get extensions from users."
"""

helps['mail usersmailfoldersmessage list-mention'] = """
    type: command
    short-summary: "Get mentions from users."
"""

helps['mail usersmailfoldersmessage list-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users."
"""

helps['mail usersmailfoldersmessage list-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users."
"""

helps['mail usersmailfoldersmessage show-attachment'] = """
    type: command
    short-summary: "Get attachments from users."
"""

helps['mail usersmailfoldersmessage show-extension'] = """
    type: command
    short-summary: "Get extensions from users."
"""

helps['mail usersmailfoldersmessage show-mention'] = """
    type: command
    short-summary: "Get mentions from users."
"""

helps['mail usersmailfoldersmessage show-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users."
"""

helps['mail usersmailfoldersmessage show-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users."
"""

helps['mail usersmailfoldersmessage update-attachment'] = """
    type: command
    short-summary: "Update the navigation property attachments in users."
"""

helps['mail usersmailfoldersmessage update-extension'] = """
    type: command
    short-summary: "Update the navigation property extensions in users."
"""

helps['mail usersmailfoldersmessage update-mention'] = """
    type: command
    short-summary: "Update the navigation property mentions in users."
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail usersmailfoldersmessage update-multi-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property multiValueExtendedProperties in users."
"""

helps['mail usersmailfoldersmessage update-single-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property singleValueExtendedProperties in users."
"""

helps['mail usersmessage'] = """
    type: group
    short-summary: Manage usersmessage with mail_beta
"""

helps['mail usersmessage create-attachment'] = """
    type: command
    short-summary: "Create new navigation property to attachments for users."
"""

helps['mail usersmessage create-extension'] = """
    type: command
    short-summary: "Create new navigation property to extensions for users."
"""

helps['mail usersmessage create-mention'] = """
    type: command
    short-summary: "Create new navigation property to mentions for users."
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail usersmessage create-multi-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to multiValueExtendedProperties for users."
"""

helps['mail usersmessage create-single-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to singleValueExtendedProperties for users."
"""

helps['mail usersmessage delete-attachment'] = """
    type: command
    short-summary: "Delete navigation property attachments for users."
"""

helps['mail usersmessage delete-extension'] = """
    type: command
    short-summary: "Delete navigation property extensions for users."
"""

helps['mail usersmessage delete-mention'] = """
    type: command
    short-summary: "Delete navigation property mentions for users."
"""

helps['mail usersmessage delete-multi-value-extended-property'] = """
    type: command
    short-summary: "Delete navigation property multiValueExtendedProperties for users."
"""

helps['mail usersmessage delete-single-value-extended-property'] = """
    type: command
    short-summary: "Delete navigation property singleValueExtendedProperties for users."
"""

helps['mail usersmessage list-attachment'] = """
    type: command
    short-summary: "Get attachments from users."
"""

helps['mail usersmessage list-extension'] = """
    type: command
    short-summary: "Get extensions from users."
"""

helps['mail usersmessage list-mention'] = """
    type: command
    short-summary: "Get mentions from users."
"""

helps['mail usersmessage list-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users."
"""

helps['mail usersmessage list-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users."
"""

helps['mail usersmessage show-attachment'] = """
    type: command
    short-summary: "Get attachments from users."
"""

helps['mail usersmessage show-extension'] = """
    type: command
    short-summary: "Get extensions from users."
"""

helps['mail usersmessage show-mention'] = """
    type: command
    short-summary: "Get mentions from users."
"""

helps['mail usersmessage show-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users."
"""

helps['mail usersmessage show-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users."
"""

helps['mail usersmessage update-attachment'] = """
    type: command
    short-summary: "Update the navigation property attachments in users."
"""

helps['mail usersmessage update-extension'] = """
    type: command
    short-summary: "Update the navigation property extensions in users."
"""

helps['mail usersmessage update-mention'] = """
    type: command
    short-summary: "Update the navigation property mentions in users."
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail usersmessage update-multi-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property multiValueExtendedProperties in users."
"""

helps['mail usersmessage update-single-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property singleValueExtendedProperties in users."
"""
