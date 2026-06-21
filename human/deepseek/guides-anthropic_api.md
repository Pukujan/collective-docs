---
title: Anthropic-Compatible API
source: deepseek
url: https://api-docs.deepseek.com/guides/anthropic_api
fetched: 2026-06-21T06:39:59.376151
---

# Anthropic-Compatible API

* [](/)
* API Guides
* Anthropic API

On this page# Anthropic API


To meet the demand for using the Anthropic API ecosystem, our API has added support for the Anthropic API format, with the `base_url` being `https://api.deepseek.com/anthropic`.


With simple configuration, you can integrate the capabilities of DeepSeek into the Anthropic API ecosystem.


## Use DeepSeek in Claude Code[​](#use-deepseek-in-claude-code)


Please refer to [Integrate with AI Tools](/guides/coding_agents).


## Invoke DeepSeek Model via Anthropic API[​](#invoke-deepseek-model-via-anthropic-api)


* Install Anthropic SDK


```
`pip install anthropic
`
```


* Config Environment Variables


```
`export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_API_KEY=${YOUR_API_KEY}
`
```


* Invoke the API


```
`import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=1000,
    system="You are a helpful assistant.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hi, how are you?"
                }
            ]
        }
    ]
)
print(message.content)
`
```


**Note:** When you pass an unsupported model name to DeepSeek's Anthropic API, the API backend will automatically map it to the `deepseek-v4-flash` model.


## Anthropic Model Mapping[​](#anthropic-model-mapping)


When you use the Anthropic API, we map the Claude model names you pass in:


* Models starting with claude-opus are mapped to deepseek-v4-pro

* Models starting with claude-haiku or claude-sonnet are mapped to deepseek-v4-flash


With this mapping, when using the developer mode of the new Claude Desktop APP, you can bypass the APP's model name restrictions by simply changing the base_url and api_key to connect to DeepSeek models.


## Anthropic API Compatibility Details[​](#anthropic-api-compatibility-details)


### HTTP Header[​](#http-header)


[TABLE]
 | Field  Support Status  |
|  anthropic-beta  Ignored  |
|  anthropic-version  Ignored  |
|  x-api-key  Fully Supported  |

[/TABLE]

### Simple Fields[​](#simple-fields)


[TABLE]
 | Field  Support Status  |
|  model  Use DeepSeek Model Instead  |
|  max_tokens  Fully Supported  |
|  container  Ignored  |
|  mcp_servers  Ignored  |
|  metadata  `user_id` is supported, others are ignored
Please refer to [Rate Limit & Isolation](/quick_start/rate_limit) for more information about `user_id` parameter.  |
|  service_tier  Ignored  |
|  stop_sequences  Fully Supported  |
|  stream  Fully Supported  |
|  system  Fully Supported  |
|  temperature  Fully Supported (range [0.0 ~ 2.0])  |
|  thinking  Supported (`budget_tokens` is ignored)  |
|  output_config  Only `effort` is supported  |
|  top_k  Ignored  |
|  top_p  Fully Supported  |

[/TABLE]

### Tool Fields[​](#tool-fields)


#### tools[​](#tools)


[TABLE]
 | Field  Support Status  |
|  name  Fully Supported  |
|  input_schema  Fully Supported  |
|  description  Fully Supported  |
|  cache_control  Ignored  |

[/TABLE]

#### tool_choice[​](#tool_choice)


[TABLE]
 | Value  Support Status  |
|  none  Fully Supported  |
|  auto  Supported (`disable_parallel_tool_use` is ignored)  |
|  any  Supported (`disable_parallel_tool_use` is ignored)  |
|  tool  Supported (`disable_parallel_tool_use` is ignored)  |

[/TABLE]

### Message Fields[​](#message-fields)


[TABLE]
|  Field  Variant  Sub-Field  Support Status  |
|   content    string     Fully Supported  |
|  array, type="text"   text    Fully Supported   |
|   cache_control    Ignored   |
|   citations    Ignored   |
|   array, type="image"      Not Supported   |
|   array, type = "document"      Not Supported   |
|   array, type = "search_result"      Not Supported   |
|   array, type = "thinking"      Supported   |
|   array, type="redacted_thinking"      Not Supported   |
|   array, type = "tool_use"    id    Fully Supported   |
|   input    Fully Supported   |
|   name    Fully Supported   |
|   cache_control    Ignored   |
|   array, type = "tool_result"    tool_use_id    Fully Supported   |
|   content    Fully Supported   |
|   cache_control    Ignored   |
|   is_error    Ignored   |
|   array, type = "server_tool_use"      Supported   |
|   array, type = "web_search_tool_result"      Supported   |
|   array, type = "code_execution_tool_result"      Not Supported   |
|   array, type = "mcp_tool_use"      Not Supported   |
|   array, type = "mcp_tool_result"      Not Supported   |
|   array, type = "container_upload"      Not Supported   |

[/TABLE]
[PreviousContext Caching](/guides/kv_cache)[NextIntroduction](/api/deepseek-api)
* [Use DeepSeek in Claude Code](#use-deepseek-in-claude-code)
* [Invoke DeepSeek Model via Anthropic API](#invoke-deepseek-model-via-anthropic-api)
* [Anthropic Model Mapping](#anthropic-model-mapping)
* [Anthropic API Compatibility Details](#anthropic-api-compatibility-details)
[HTTP Header](#http-header)
* [Simple Fields](#simple-fields)
* [Tool Fields](#tool-fields)
* [Message Fields](#message-fields)