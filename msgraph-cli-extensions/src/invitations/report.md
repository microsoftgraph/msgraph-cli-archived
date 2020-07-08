# Azure CLI Module Creation Report

### invitations invitation get-invited-user

get-invited-user a invitations invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|invitations invitation|invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-invited-user|GetInvitedUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: invitation-id of invitation|invitation_id|invitation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### invitations invitation-invitation create-invitation

create-invitation a invitations invitation-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|invitations invitation-invitation|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-invitation|CreateInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--invited-user-display-name**|string|The display name of the user being invited.|invited_user_display_name|invitedUserDisplayName|
|**--invited-user-type**|string|The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.|invited_user_type|invitedUserType|
|**--invited-user-email-address**|string|The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.|invited_user_email_address|invitedUserEmailAddress|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--invite-redirect-url**|string|The URL user should be redirected to once the invitation is redeemed. Required.|invite_redirect_url|inviteRedirectUrl|
|**--invite-redeem-url**|string|The URL user can use to redeem his invitation. Read-Only|invite_redeem_url|inviteRedeemUrl|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--reset-redemption**|boolean||reset_redemption|resetRedemption|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--invited-user-message-info-cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--invited-user-message-info-message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|
|**--invited-user-message-info-customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|

### invitations invitation-invitation delete

delete a invitations invitation-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|invitations invitation-invitation|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: invitation-id of invitation|invitation_id|invitation-id|
|**--if-match**|string|ETag|if_match|If-Match|

### invitations invitation-invitation get-invitation

get-invitation a invitations invitation-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|invitations invitation-invitation|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-invitation|GetInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: invitation-id of invitation|invitation_id|invitation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### invitations invitation-invitation list-invitation

list-invitation a invitations invitation-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|invitations invitation-invitation|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-invitation|ListInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### invitations invitation-invitation update

update a invitations invitation-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|invitations invitation-invitation|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: invitation-id of invitation|invitation_id|invitation-id|
|**--id**|string|Read-only.|id|id|
|**--invited-user-display-name**|string|The display name of the user being invited.|invited_user_display_name|invitedUserDisplayName|
|**--invited-user-type**|string|The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.|invited_user_type|invitedUserType|
|**--invited-user-email-address**|string|The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.|invited_user_email_address|invitedUserEmailAddress|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--invite-redirect-url**|string|The URL user should be redirected to once the invitation is redeemed. Required.|invite_redirect_url|inviteRedirectUrl|
|**--invite-redeem-url**|string|The URL user can use to redeem his invitation. Read-Only|invite_redeem_url|inviteRedeemUrl|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--reset-redemption**|boolean||reset_redemption|resetRedemption|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--invited-user-message-info-cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--invited-user-message-info-message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|
|**--invited-user-message-info-customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
