# OpenAI Chat Completions API

[Course index](../../README.md) · [Original source](https://platform.openai.com/docs/api-reference/chat/create) · [Raw file](../../raw/optional-readings/ref-5acff3b63a58.html)

Retrieved: 2026-11-13T16:54:37.944797+00:00

Copy Markdown

# Chat

#### ChatCompletions

Given a list of messages comprising a conversation, the model will return a response.

##### [Create chat completion](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create)

POST

/chat/completions

##### [Delete chat completion](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/delete)

DELETE

/chat/completions/{completion\_id}

##### [List Chat Completions](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/list)

GET

/chat/completions

##### [Get chat completion](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/retrieve)

GET

/chat/completions/{completion\_id}

##### [Update chat completion](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/update)

POST

/chat/completions/{completion\_id}

##### ModelsExpand Collapse

ChatCompletionAllowedTools object { mode, tools }

Constrains the tools available to the model to a pre-defined set.

mode: "auto" or "required" Constrains the tools available to the model to a pre-defined set.
auto allows the model to pick from among the allowed tools and generate a
message.
required requires the model to call one or more of the allowed tools.
One of the following: "auto" "required" tools: array of map[unknown] A list of tool definitions that the model should be allowed to call.
For the Chat Completions API, the list of tool definitions might look like:
[
{ "type": "function", "function": { "name": "get\_weather" } },
{ "type": "function", "function": { "name": "get\_time" } }
]

ChatCompletion object { id, choices, created, 7 more }

Represents a chat completion response returned by model, based on the provided input.

id: string A unique identifier for the chat completion.
choices: array of { finish\_reason, index, logprobs, message } A list of chat completion choices. Can be more than one if n is greater than 1.
finish\_reason: "stop" or "length" or "tool\_calls" or 2 more The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence,
length if the maximum number of tokens specified in the request was reached,
content\_filter if content was omitted due to a flag from our content filters,
tool\_calls if the model called a tool, or function\_call (deprecated) if the model called a function.
Read the Model Spec for more.
One of the following: "stop" "length" "tool\_calls" "content\_filter" "function\_call" index: integer The index of the choice in the list of choices.
logprobs: object or null Log probability information for the choice.
content: array of ChatCompletionTokenLogprob or null A list of message content tokens with log probability information.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
top\_logprobs: array of { token, bytes, logprob } List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested top\_logprobs.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
refusal: array of ChatCompletionTokenLogprob or null A list of message refusal tokens with log probability information.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
top\_logprobs: array of { token, bytes, logprob } List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested top\_logprobs.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
message: ChatCompletionMessage { content, role, annotations, 4 more } A chat completion message generated by the model.
created: integer The Unix timestamp (in seconds) of when the chat completion was created.
formatunixtime model: string The model used for the chat completion.
object: "chat.completion" The object type, which is always chat.completion.
metadata: optional Metadata or null Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.
moderation: optional object or null Moderation results for the request input and generated output, if moderated
completions were requested.
input: ModerationResults or Error Moderation for the request input.
One of the following: ModerationResults { model, results, type } Successful moderation results for the request input or generated output.
model: string The moderation model used to generate the results.
results: array of { categories, category\_applied\_input\_types, category\_scores, 3 more } A list of moderation results.
categories: map[boolean] A dictionary of moderation categories to booleans, True if the input is flagged under this category.
category\_applied\_input\_types: map[array of "text" or "image"] Which modalities of input are reflected by the score for each category.
One of the following: "text" "image" category\_scores: map[number] A dictionary of moderation categories to scores.
flagged: boolean A boolean indicating whether the content was flagged by any category.
model: string The moderation model that produced this result.
type: "moderation\_result" (default: "moderation\_result") The object type, which was always moderation\_result for successful moderation results.
type: "moderation\_results" The object type, which is always moderation\_results.
Error { code, message, type } An error produced while attempting moderation.
code: string The error code.
message: string The error message.
type: "error" The object type, which is always error.
output: ModerationResults or Error Moderation for the generated output.
One of the following: ModerationResults { model, results, type } Successful moderation results for the request input or generated output.
model: string The moderation model used to generate the results.
results: array of { categories, category\_applied\_input\_types, category\_scores, 3 more } A list of moderation results.
categories: map[boolean] A dictionary of moderation categories to booleans, True if the input is flagged under this category.
category\_applied\_input\_types: map[array of "text" or "image"] Which modalities of input are reflected by the score for each category.
One of the following: "text" "image" category\_scores: map[number] A dictionary of moderation categories to scores.
flagged: boolean A boolean indicating whether the content was flagged by any category.
model: string The moderation model that produced this result.
type: "moderation\_result" (default: "moderation\_result") The object type, which was always moderation\_result for successful moderation results.
type: "moderation\_results" The object type, which is always moderation\_results.
Error { code, message, type } An error produced while attempting moderation.
code: string The error code.
message: string The error message.
type: "error" The object type, which is always error.
service\_tier: optional "auto" or "default" or "flex" or 3 more or null (default: "auto") Specifies the processing type used for serving the request.
If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
If set to ‘flex’, then the request will be processed with the Flex Processing service tier.
To opt-in to Fast mode at the request level, include the service\_tier=fast or service\_tier=priority parameter for Responses or Chat Completions. The response will show service\_tier=priority regardless of if you specify service\_tier=fast or priority in your request.
When not set, the default behavior is ‘auto’.
When the service\_tier parameter is set, the response body will include the service\_tier value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
One of the following: "auto" "default" "flex" "scale" "priority" "fast" system\_fingerprint: optional string Deprecated.
This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the seed request parameter to understand when backend changes have been made that might impact determinism.
usage: optional CompletionUsage { completion\_tokens, prompt\_tokens, total\_tokens, 2 more } Usage statistics for the completion request.

ChatCompletionAllowedToolChoice object { allowed\_tools, type }

Constrains the tools available to the model to a pre-defined set.

allowed\_tools: [ChatCompletionAllowedTools](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)) { mode, tools }

Constrains the tools available to the model to a pre-defined set.

type: "allowed\_tools"

Allowed tool configuration type. Always `allowed_tools`.

ChatCompletionAssistantMessageParam object { role, audio, content, 4 more }

Messages sent by the model in response to user messages.

role: "assistant" The role of the messages author, in this case assistant.
audio: optional object or null Data about a previous audio response from the model.
Learn more.
id: string Unique identifier for a previous audio response from the model.
content: optional string or array of ChatCompletionContentPartText or ChatCompletionContentPartRefusal or null The contents of the assistant message. Required unless tool\_calls or function\_call is specified.
One of the following: TextContent = string The contents of the assistant message.
ArrayOfContentParts = array of ChatCompletionContentPartText or ChatCompletionContentPartRefusal An array of content parts with a defined type. Can be one or more of type text, or exactly one of type refusal.
minItems1 One of the following: ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } Learn about text inputs.
text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartRefusal { refusal, type } refusal: string The refusal message generated by the model.
type: "refusal" The type of the content part.
function\_call: optional object or null Deprecated.
Deprecated and replaced by tool\_calls. The name and arguments of a function that should be called, as generated by the model.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.
refusal: optional string or null The refusal message by the assistant.
tool\_calls: optional array of ChatCompletionMessageToolCall The tool calls generated by the model, such as function calls.
One of the following: ChatCompletionMessageFunctionToolCall { id, function, type } A call to a function tool created by the model.
id: string The ID of the tool call.
function: { arguments, name } The function that the model called.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
type: "function" The type of the tool. Currently, only function is supported.
ChatCompletionMessageCustomToolCall { id, custom, type } A call to a custom tool created by the model.
id: string The ID of the tool call.
custom: { input, name } The custom tool that the model called.
input: string The input for the custom tool call generated by the model.
name: string The name of the custom tool to call.
type: "custom" The type of the tool. Always custom.

ChatCompletionAudio object { id, data, expires\_at, transcript }

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://developers.openai.com/api/docs/guides/audio).

id: string Unique identifier for this audio response.
data: string Base64 encoded audio bytes generated by the model, in the format
specified in the request.
expires\_at: integer The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.
formatunixtime transcript: string Transcript of the audio generated by the model.

ChatCompletionAudioParam object { format, voice }

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://developers.openai.com/api/docs/guides/audio).

format: "wav" or "aac" or "mp3" or 3 more Specifies the output audio format. Must be one of wav, mp3, flac,
opus, or pcm16.
One of the following: "wav" "aac" "mp3" "flac" "opus" "pcm16" voice: string or "alloy" or "ash" or "ballad" or 7 more or ID The voice the model uses to respond. Supported built-in voices are
alloy, ash, ballad, coral, echo, fable, nova, onyx,
sage, shimmer, marin, and cedar. You may also provide a
custom voice object with an id, for example { "id": "voice\_1234" }.
Custom voices must be created from audio samples. Voices created from text
prompts are supported only in Live.
One of the following: string "alloy" or "ash" or "ballad" or 7 more One of the following: "alloy" "ash" "ballad" "coral" "echo" "sage" "shimmer" "verse" "marin" "cedar" ID { id } Custom voice reference.
id: string The custom voice ID, e.g. voice\_1234.

ChatCompletionChunk object { id, choices, created, 7 more }

Represents a streamed chunk of a chat completion response returned
by the model, based on the provided input.
[Learn more](https://developers.openai.com/api/docs/guides/streaming-responses).

id: string A unique identifier for the chat completion. Each chunk has the same ID.
choices: array of { delta, index, finish\_reason, logprobs } A list of chat completion choices. Can contain more than one elements if n is greater than 1. Can also be empty for the
last chunk if you set stream\_options: {"include\_usage": true}.
delta: { audio, content, function\_call, 3 more } A chat completion delta generated by streamed model responses.
Streamed audio can arrive in partial updates with an ID, base64 data, or
transcript text. The final audio update contains only its expiry timestamp.
audio: optional { id, data, expires\_at, transcript } A partial audio response. Audio chunks may carry an ID, base64 data, or
transcript text; the final audio update contains only its expiry timestamp.
id: optional string Unique identifier for this audio response.
data: optional string Base64 encoded audio bytes generated by the model, in the format
specified in the request.
expires\_at: optional integer The Unix timestamp (in seconds) for when this audio response will no
longer be accessible on the server for use in multi-turn conversations.
formatunixtime transcript: optional string Transcript text from this audio chunk.
content: optional string or null The contents of the chunk message.
function\_call: optional { arguments, name } Deprecated.
Deprecated and replaced by tool\_calls. The name and arguments of a function that should be called, as generated by the model.
arguments: optional string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: optional string The name of the function to call.
refusal: optional string or null The refusal message generated by the model.
role: optional "developer" or "system" or "user" or 2 more The role of the author of this message.
One of the following: "developer" "system" "user" "assistant" "tool" tool\_calls: optional array of { index, id, function, type } index: integer id: optional string The ID of the tool call.
function: optional { arguments, name } arguments: optional string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: optional string The name of the function to call.
type: optional "function" The type of the tool. Currently, only function is supported.
index: integer The index of the choice in the list of choices.
finish\_reason: optional "stop" or "length" or "tool\_calls" or 2 more or null The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence,
length if the maximum number of tokens specified in the request was reached,
content\_filter if content was omitted due to a flag from our content filters,
tool\_calls if the model called a tool, or function\_call (deprecated) if the model called a function.
Omitted from the final audio update containing only delta.audio.expires\_at.
One of the following: "stop" "length" "tool\_calls" "content\_filter" "function\_call" logprobs: optional object or null Log probability information for the choice.
content: array of ChatCompletionTokenLogprob or null A list of message content tokens with log probability information.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
top\_logprobs: array of { token, bytes, logprob } List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested top\_logprobs.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
refusal: array of ChatCompletionTokenLogprob or null A list of message refusal tokens with log probability information.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
top\_logprobs: array of { token, bytes, logprob } List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested top\_logprobs.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
created: integer The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.
formatunixtime model: string The model to generate the completion.
object: "chat.completion.chunk" The object type, which is always chat.completion.chunk.
moderation: optional object or null Moderation results for the request input and generated output. Present
on the moderation chunk when moderated completions are requested.
input: ModerationResults or Error Moderation for the request input.
One of the following: ModerationResults { model, results, type } Successful moderation results for the request input or generated output.
model: string The moderation model used to generate the results.
results: array of { categories, category\_applied\_input\_types, category\_scores, 3 more } A list of moderation results.
categories: map[boolean] A dictionary of moderation categories to booleans, True if the input is flagged under this category.
category\_applied\_input\_types: map[array of "text" or "image"] Which modalities of input are reflected by the score for each category.
One of the following: "text" "image" category\_scores: map[number] A dictionary of moderation categories to scores.
flagged: boolean A boolean indicating whether the content was flagged by any category.
model: string The moderation model that produced this result.
type: "moderation\_result" (default: "moderation\_result") The object type, which was always moderation\_result for successful moderation results.
type: "moderation\_results" The object type, which is always moderation\_results.
Error { code, message, type } An error produced while attempting moderation.
code: string The error code.
message: string The error message.
type: "error" The object type, which is always error.
output: ModerationResults or Error Moderation for the generated output.
One of the following: ModerationResults { model, results, type } Successful moderation results for the request input or generated output.
model: string The moderation model used to generate the results.
results: array of { categories, category\_applied\_input\_types, category\_scores, 3 more } A list of moderation results.
categories: map[boolean] A dictionary of moderation categories to booleans, True if the input is flagged under this category.
category\_applied\_input\_types: map[array of "text" or "image"] Which modalities of input are reflected by the score for each category.
One of the following: "text" "image" category\_scores: map[number] A dictionary of moderation categories to scores.
flagged: boolean A boolean indicating whether the content was flagged by any category.
model: string The moderation model that produced this result.
type: "moderation\_result" (default: "moderation\_result") The object type, which was always moderation\_result for successful moderation results.
type: "moderation\_results" The object type, which is always moderation\_results.
Error { code, message, type } An error produced while attempting moderation.
code: string The error code.
message: string The error message.
type: "error" The object type, which is always error.
obfuscation: optional string An obfuscation string added to normalize the size of streamed chunks as a
mitigation to certain side-channel attacks. The field is included by
default and omitted when stream\_options.include\_obfuscation is false.
service\_tier: optional "auto" or "default" or "flex" or 3 more or null (default: "auto") Specifies the processing type used for serving the request.
If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
If set to ‘flex’, then the request will be processed with the Flex Processing service tier.
To opt-in to Fast mode at the request level, include the service\_tier=fast or service\_tier=priority parameter for Responses or Chat Completions. The response will show service\_tier=priority regardless of if you specify service\_tier=fast or priority in your request.
When not set, the default behavior is ‘auto’.
When the service\_tier parameter is set, the response body will include the service\_tier value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
One of the following: "auto" "default" "flex" "scale" "priority" "fast" system\_fingerprint: optional string Deprecated.
This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the seed request parameter to understand when backend changes have been made that might impact determinism.
usage: optional CompletionUsage or null An optional field that will only be present when you set
stream\_options: {"include\_usage": true} in your request. When present, it
contains a null value except for the last chunk which contains the
token usage statistics for the entire request.
NOTE: If the stream is interrupted or cancelled, you may not
receive the final usage chunk which contains the total token usage for
the request.

ChatCompletionContentPart = [ChatCompletionContentPartText](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ChatCompletionContentPartImage](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)) { image\_url, type, prompt\_cache\_breakpoint }  or [ChatCompletionContentPartInputAudio](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)) { input\_audio, type, prompt\_cache\_breakpoint }  or FileContentPart { file, type, prompt\_cache\_breakpoint }

Learn about [text inputs](https://developers.openai.com/api/docs/guides/text).

One of the following: ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } Learn about text inputs.
text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartImage { image\_url, type, prompt\_cache\_breakpoint } Learn about image inputs.
image\_url: { url, detail } url: string Either a URL of the image or the base64 encoded image data.
formaturi detail: optional "auto" or "low" or "high" or "original" (default: "auto") Specifies the detail level of the image. Learn more in the Vision guide.
One of the following: "auto" "low" "high" "original" type: "image\_url" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartInputAudio { input\_audio, type, prompt\_cache\_breakpoint } Learn about audio inputs.
input\_audio: { data, format } data: string Base64 encoded audio data.
format: "wav" or "mp3" The format of the encoded audio data. Currently supports “wav” and “mp3”.
One of the following: "wav" "mp3" type: "input\_audio" The type of the content part. Always input\_audio.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" FileContentPart { file, type, prompt\_cache\_breakpoint } Learn about file inputs for text generation.
file: { file\_data, file\_id, filename } file\_data: optional string The base64 encoded file data, used when passing the file to the model
as a string.
file\_id: optional string The ID of an uploaded file to use as input.
filename: optional string The name of the file, used when passing the file to the model as a
string.
type: "file" The type of the content part. Always file.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h"

ChatCompletionContentPartImage object { image\_url, type, prompt\_cache\_breakpoint }

Learn about [image inputs](https://developers.openai.com/api/docs/guides/images-vision).

image\_url: { url, detail } url: string Either a URL of the image or the base64 encoded image data.
formaturi detail: optional "auto" or "low" or "high" or "original" (default: "auto") Specifies the detail level of the image. Learn more in the Vision guide.
One of the following: "auto" "low" "high" "original" type: "image\_url" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h"

ChatCompletionContentPartInputAudio object { input\_audio, type, prompt\_cache\_breakpoint }

Learn about [audio inputs](https://developers.openai.com/api/docs/guides/audio).

input\_audio: { data, format } data: string Base64 encoded audio data.
format: "wav" or "mp3" The format of the encoded audio data. Currently supports “wav” and “mp3”.
One of the following: "wav" "mp3" type: "input\_audio" The type of the content part. Always input\_audio.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h"

ChatCompletionContentPartRefusal object { refusal, type }

refusal: string

The refusal message generated by the model.

type: "refusal"

The type of the content part.

ChatCompletionContentPartText object { text, type, prompt\_cache\_breakpoint }

Learn about [text inputs](https://developers.openai.com/api/docs/guides/text).

text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h"

ChatCompletionCustomTool object { custom, type }

A custom tool that processes input using a specified format.

custom: { name, description, format } Properties of the custom tool.
name: string The name of the custom tool, used to identify it in tool calls.
description: optional string Optional description of the custom tool, used to provide more context.
format: optional Text or Grammar The input format for the custom tool. Default is unconstrained text.
One of the following: Text { type } Unconstrained free-form text.
type: "text" Unconstrained text format. Always text.
Grammar { grammar, type } A grammar defined by the user.
grammar: { definition, syntax } Your chosen grammar.
definition: string The grammar definition.
syntax: "lark" or "regex" The syntax of the grammar definition. One of lark or regex.
One of the following: "lark" "regex" type: "grammar" Grammar format. Always grammar.
type: "custom" The type of the custom tool. Always custom.

ChatCompletionDeleted object { id, deleted, object }

id: string The ID of the chat completion that was deleted.
deleted: boolean Whether the chat completion was deleted.
object: "chat.completion.deleted" The type of object being deleted.

ChatCompletionDeveloperMessageParam object { content, role, name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

content: string or array of ChatCompletionContentPartText The contents of the developer message.
One of the following: TextContent = string The contents of the developer message.
ArrayOfContentParts = array of ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } An array of content parts with a defined type. For developer messages, only type text is supported.
minItems1 text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "developer" The role of the messages author, in this case developer.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.

ChatCompletionFunctionCallOption object { name }

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

name: string

The name of the function to call.

ChatCompletionFunctionMessageParam object { content, name, role }

content: string or null The contents of the function message.
name: string The name of the function to call.
role: "function" The role of the messages author, in this case function.

ChatCompletionFunctionTool object { function, type }

A function tool that can be used to generate a response.

function: [FunctionDefinition](https://developers.openai.com/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of the tool. Currently, only `function` is supported.

ChatCompletionMessage object { content, role, annotations, 4 more }

A chat completion message generated by the model.

content: string or null The contents of the message.
role: "assistant" The role of the author of this message.
annotations: optional array of { type, url\_citation } Annotations for the message, when applicable, as when using the
web search tool.
type: "url\_citation" The type of the URL citation. Always url\_citation.
url\_citation: { end\_index, start\_index, title, url } A URL citation when using web search.
end\_index: integer The index of the last character of the URL citation in the message.
start\_index: integer The index of the first character of the URL citation in the message.
title: string The title of the web resource.
url: string The URL of the web resource.
formaturi audio: optional ChatCompletionAudio or null If the audio output modality is requested, this object contains data
about the audio response from the model. Learn more.
function\_call: optional object or null Deprecated.
Deprecated and replaced by tool\_calls. The name and arguments of a function that should be called, as generated by the model.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
refusal: optional string or null The refusal message generated by the model.
tool\_calls: optional array of ChatCompletionMessageToolCall or null The tool calls generated by the model, such as function calls.
One of the following: ChatCompletionMessageFunctionToolCall { id, function, type } A call to a function tool created by the model.
id: string The ID of the tool call.
function: { arguments, name } The function that the model called.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
type: "function" The type of the tool. Currently, only function is supported.
ChatCompletionMessageCustomToolCall { id, custom, type } A call to a custom tool created by the model.
id: string The ID of the tool call.
custom: { input, name } The custom tool that the model called.
input: string The input for the custom tool call generated by the model.
name: string The name of the custom tool to call.
type: "custom" The type of the tool. Always custom.

ChatCompletionMessageCustomToolCall object { id, custom, type }

A call to a custom tool created by the model.

id: string The ID of the tool call.
custom: { input, name } The custom tool that the model called.
input: string The input for the custom tool call generated by the model.
name: string The name of the custom tool to call.
type: "custom" The type of the tool. Always custom.

ChatCompletionMessageFunctionToolCall object { id, function, type }

A call to a function tool created by the model.

id: string The ID of the tool call.
function: { arguments, name } The function that the model called.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
type: "function" The type of the tool. Currently, only function is supported.

ChatCompletionMessageParam = [ChatCompletionDeveloperMessageParam](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)) { content, role, name }  or [ChatCompletionSystemMessageParam](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)) { content, role, name }  or [ChatCompletionUserMessageParam](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)) { content, role, name }  or 3 more

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

One of the following: ChatCompletionDeveloperMessageParam { content, role, name } Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, developer messages
replace the previous system messages.
content: string or array of ChatCompletionContentPartText The contents of the developer message.
One of the following: TextContent = string The contents of the developer message.
ArrayOfContentParts = array of ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } An array of content parts with a defined type. For developer messages, only type text is supported.
minItems1 text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "developer" The role of the messages author, in this case developer.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.
ChatCompletionSystemMessageParam { content, role, name } Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use developer messages
for this purpose instead.
content: string or array of ChatCompletionContentPartText The contents of the system message.
One of the following: TextContent = string The contents of the system message.
ArrayOfContentParts = array of ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } An array of content parts with a defined type. For system messages, only type text is supported.
minItems1 text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "system" The role of the messages author, in this case system.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.
ChatCompletionUserMessageParam { content, role, name } Messages sent by an end user, containing prompts or additional context
information.
content: string or array of ChatCompletionContentPart The contents of the user message.
One of the following: TextContent = string The text contents of the message.
ArrayOfContentParts = array of ChatCompletionContentPart An array of content parts with a defined type. Supported options differ based on the model being used to generate the response. Can contain text, image, or audio inputs.
minItems1 One of the following: ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } Learn about text inputs.
text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartImage { image\_url, type, prompt\_cache\_breakpoint } Learn about image inputs.
image\_url: { url, detail } url: string Either a URL of the image or the base64 encoded image data.
formaturi detail: optional "auto" or "low" or "high" or "original" (default: "auto") Specifies the detail level of the image. Learn more in the Vision guide.
One of the following: "auto" "low" "high" "original" type: "image\_url" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartInputAudio { input\_audio, type, prompt\_cache\_breakpoint } Learn about audio inputs.
input\_audio: { data, format } data: string Base64 encoded audio data.
format: "wav" or "mp3" The format of the encoded audio data. Currently supports “wav” and “mp3”.
One of the following: "wav" "mp3" type: "input\_audio" The type of the content part. Always input\_audio.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" FileContentPart { file, type, prompt\_cache\_breakpoint } Learn about file inputs for text generation.
file: { file\_data, file\_id, filename } file\_data: optional string The base64 encoded file data, used when passing the file to the model
as a string.
file\_id: optional string The ID of an uploaded file to use as input.
filename: optional string The name of the file, used when passing the file to the model as a
string.
type: "file" The type of the content part. Always file.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "user" The role of the messages author, in this case user.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.
ChatCompletionAssistantMessageParam { role, audio, content, 4 more } Messages sent by the model in response to user messages.
role: "assistant" The role of the messages author, in this case assistant.
audio: optional object or null Data about a previous audio response from the model.
Learn more.
id: string Unique identifier for a previous audio response from the model.
content: optional string or array of ChatCompletionContentPartText or ChatCompletionContentPartRefusal or null The contents of the assistant message. Required unless tool\_calls or function\_call is specified.
One of the following: TextContent = string The contents of the assistant message.
ArrayOfContentParts = array of ChatCompletionContentPartText or ChatCompletionContentPartRefusal An array of content parts with a defined type. Can be one or more of type text, or exactly one of type refusal.
minItems1 One of the following: ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } Learn about text inputs.
text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartRefusal { refusal, type } refusal: string The refusal message generated by the model.
type: "refusal" The type of the content part.
function\_call: optional object or null Deprecated.
Deprecated and replaced by tool\_calls. The name and arguments of a function that should be called, as generated by the model.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.
refusal: optional string or null The refusal message by the assistant.
tool\_calls: optional array of ChatCompletionMessageToolCall The tool calls generated by the model, such as function calls.
One of the following: ChatCompletionMessageFunctionToolCall { id, function, type } A call to a function tool created by the model.
id: string The ID of the tool call.
function: { arguments, name } The function that the model called.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
type: "function" The type of the tool. Currently, only function is supported.
ChatCompletionMessageCustomToolCall { id, custom, type } A call to a custom tool created by the model.
id: string The ID of the tool call.
custom: { input, name } The custom tool that the model called.
input: string The input for the custom tool call generated by the model.
name: string The name of the custom tool to call.
type: "custom" The type of the tool. Always custom.
ChatCompletionToolMessageParam { content, role, tool\_call\_id } content: string or array of ChatCompletionContentPartText The contents of the tool message.
One of the following: TextContent = string The contents of the tool message.
ArrayOfContentParts = array of ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } An array of content parts with a defined type. For tool messages, only type text is supported.
minItems1 text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "tool" The role of the messages author, in this case tool.
tool\_call\_id: string Tool call that this message is responding to.
ChatCompletionFunctionMessageParam { content, name, role } content: string or null The contents of the function message.
name: string The name of the function to call.
role: "function" The role of the messages author, in this case function.

ChatCompletionMessageToolCall = [ChatCompletionMessageFunctionToolCall](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)) { id, function, type }  or [ChatCompletionMessageCustomToolCall](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)) { id, custom, type }

A call to a function tool created by the model.

One of the following: ChatCompletionMessageFunctionToolCall { id, function, type } A call to a function tool created by the model.
id: string The ID of the tool call.
function: { arguments, name } The function that the model called.
arguments: string The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
name: string The name of the function to call.
type: "function" The type of the tool. Currently, only function is supported.
ChatCompletionMessageCustomToolCall { id, custom, type } A call to a custom tool created by the model.
id: string The ID of the tool call.
custom: { input, name } The custom tool that the model called.
input: string The input for the custom tool call generated by the model.
name: string The name of the custom tool to call.
type: "custom" The type of the tool. Always custom.

ChatCompletionModality = "text" or "audio"

One of the following:

"text"

"audio"

ChatCompletionNamedToolChoice object { function, type }

Specifies a tool the model should use. Use to force the model to call a specific function.

function: { name } name: string The name of the function to call.
type: "function" For function calling, the type is always function.

ChatCompletionNamedToolChoiceCustom object { custom, type }

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

custom: { name } name: string The name of the custom tool to call.
type: "custom" For custom tool calling, the type is always custom.

ChatCompletionPredictionContent object { content, type }

Static predicted output content, such as the content of a text file that is
being regenerated.

content: string or array of ChatCompletionContentPartText The content that should be matched when generating a model response.
If generated tokens would match this content, the entire model response
can be returned much more quickly.
One of the following: TextContent = string The content used for a Predicted Output. This is often the
text of a file you are regenerating with minor changes.
ArrayOfContentParts = array of ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } An array of content parts with a defined type. Supported options differ based on the model being used to generate the response. Can contain text inputs.
minItems1 text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" type: "content" The type of the predicted content you want to provide. This type is
currently always content.

ChatCompletionRole = "developer" or "system" or "user" or 3 more

The role of the author of a message

One of the following: "developer" "system" "user" "assistant" "tool" "function"

ChatCompletionStoreMessage object { id, content, content\_parts, 2 more }

id: string content: string or null content\_parts: array of object or null type: "text" or "image\_url" or "input\_audio" or "file" One of the following: "text" "image\_url" "input\_audio" "file" file: optional object or null file\_data: optional string or null file\_id: optional string or null filename: optional string or null image\_url: optional object or null url: string detail: optional string or null input\_audio: optional object or null data: string format: string text: optional string or null role: "user" or "assistant" or "tool" or 3 more One of the following: "user" "assistant" "tool" "system" "function" "developer" name: optional string or null

ChatCompletionStreamOptions object { include\_obfuscation, include\_usage }

Options for streaming response. Only set this when you set `stream: true`.

include\_obfuscation: optional boolean

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

include\_usage: optional boolean

If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

ChatCompletionSystemMessageParam object { content, role, name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

content: string or array of ChatCompletionContentPartText The contents of the system message.
One of the following: TextContent = string The contents of the system message.
ArrayOfContentParts = array of ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } An array of content parts with a defined type. For system messages, only type text is supported.
minItems1 text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "system" The role of the messages author, in this case system.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.

ChatCompletionTokenLogprob object { token, bytes, logprob, top\_logprobs }

token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.
top\_logprobs: array of { token, bytes, logprob } List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested top\_logprobs.
token: string The token.
bytes: array of number or null A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
logprob: number The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely.

ChatCompletionTool = [ChatCompletionFunctionTool](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type }  or [ChatCompletionCustomTool](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)) { custom, type }

A function tool that can be used to generate a response.

One of the following: ChatCompletionFunctionTool { function, type } A function tool that can be used to generate a response.
function: FunctionDefinition { name, description, parameters, strict } type: "function" The type of the tool. Currently, only function is supported.
ChatCompletionCustomTool { custom, type } A custom tool that processes input using a specified format.
custom: { name, description, format } Properties of the custom tool.
name: string The name of the custom tool, used to identify it in tool calls.
description: optional string Optional description of the custom tool, used to provide more context.
format: optional Text or Grammar The input format for the custom tool. Default is unconstrained text.
One of the following: Text { type } Unconstrained free-form text.
type: "text" Unconstrained text format. Always text.
Grammar { grammar, type } A grammar defined by the user.
grammar: { definition, syntax } Your chosen grammar.
definition: string The grammar definition.
syntax: "lark" or "regex" The syntax of the grammar definition. One of lark or regex.
One of the following: "lark" "regex" type: "grammar" Grammar format. Always grammar.
type: "custom" The type of the custom tool. Always custom.

ChatCompletionToolChoiceOption = "none" or "auto" or "required" or [ChatCompletionAllowedToolChoice](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema)) { allowed\_tools, type }  or [ChatCompletionNamedToolChoice](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)) { function, type }  or [ChatCompletionNamedToolChoiceCustom](ref-5acff3b63a58.md)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)) { custom, type }

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

One of the following: ToolChoiceMode = "none" or "auto" or "required" none means the model will not call any tool and instead generates a message. auto means the model can pick between generating a message or calling one or more tools. required means the model must call one or more tools.
One of the following: "none" "auto" "required" ChatCompletionAllowedToolChoice { allowed\_tools, type } Constrains the tools available to the model to a pre-defined set.
allowed\_tools: ChatCompletionAllowedTools { mode, tools } Constrains the tools available to the model to a pre-defined set.
type: "allowed\_tools" Allowed tool configuration type. Always allowed\_tools.
ChatCompletionNamedToolChoice { function, type } Specifies a tool the model should use. Use to force the model to call a specific function.
function: { name } name: string The name of the function to call.
type: "function" For function calling, the type is always function.
ChatCompletionNamedToolChoiceCustom { custom, type } Specifies a tool the model should use. Use to force the model to call a specific custom tool.
custom: { name } name: string The name of the custom tool to call.
type: "custom" For custom tool calling, the type is always custom.

ChatCompletionToolMessageParam object { content, role, tool\_call\_id }

content: string or array of ChatCompletionContentPartText The contents of the tool message.
One of the following: TextContent = string The contents of the tool message.
ArrayOfContentParts = array of ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } An array of content parts with a defined type. For tool messages, only type text is supported.
minItems1 text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "tool" The role of the messages author, in this case tool.
tool\_call\_id: string Tool call that this message is responding to.

ChatCompletionUserMessageParam object { content, role, name }

Messages sent by an end user, containing prompts or additional context
information.

content: string or array of ChatCompletionContentPart The contents of the user message.
One of the following: TextContent = string The text contents of the message.
ArrayOfContentParts = array of ChatCompletionContentPart An array of content parts with a defined type. Supported options differ based on the model being used to generate the response. Can contain text, image, or audio inputs.
minItems1 One of the following: ChatCompletionContentPartText { text, type, prompt\_cache\_breakpoint } Learn about text inputs.
text: string The text content.
type: "text" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartImage { image\_url, type, prompt\_cache\_breakpoint } Learn about image inputs.
image\_url: { url, detail } url: string Either a URL of the image or the base64 encoded image data.
formaturi detail: optional "auto" or "low" or "high" or "original" (default: "auto") Specifies the detail level of the image. Learn more in the Vision guide.
One of the following: "auto" "low" "high" "original" type: "image\_url" The type of the content part.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" ChatCompletionContentPartInputAudio { input\_audio, type, prompt\_cache\_breakpoint } Learn about audio inputs.
input\_audio: { data, format } data: string Base64 encoded audio data.
format: "wav" or "mp3" The format of the encoded audio data. Currently supports “wav” and “mp3”.
One of the following: "wav" "mp3" type: "input\_audio" The type of the content part. Always input\_audio.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" FileContentPart { file, type, prompt\_cache\_breakpoint } Learn about file inputs for text generation.
file: { file\_data, file\_id, filename } file\_data: optional string The base64 encoded file data, used when passing the file to the model
as a string.
file\_id: optional string The ID of an uploaded file to use as input.
filename: optional string The name of the file, used when passing the file to the model as a
string.
type: "file" The type of the content part. Always file.
prompt\_cache\_breakpoint: optional { mode, ttl } Marks the exact end of a reusable prompt prefix. When ttl is omitted, the breakpoint inherits the request’s prompt\_cache\_options.ttl; the boundary is not rounded to a token block.
mode: "explicit" (default: "explicit") The breakpoint mode. Always explicit.
ttl: optional "30m" or "12h" The minimum lifetime of this cache breakpoint. Defaults to the request TTL.
One of the following: "30m" "12h" role: "user" The role of the messages author, in this case user.
name: optional string An optional name for the participant. Provides the model information to differentiate between participants of the same role.

#### ChatCompletionsMessages

Given a list of messages comprising a conversation, the model will return a response.

##### [Get chat messages](https://developers.openai.com/api/reference/resources/chat/subresources/completions/subresources/messages/methods/list)

GET

/chat/completions/{completion\_id}/messages
