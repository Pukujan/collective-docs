# Specification
* [Overview](#overview)
* [Key Details](#key-details)
[Base Protocol](#base-protocol)
* [Features](#features)
* [Additional Utilities](#additional-utilities)
* [Security and Trust & Safety](#security-and-trust-%26-safety)
[Key Principles](#key-principles)
* [Implementation Guidelines](#implementation-guidelines)
* [Learn More](#learn-more)
# Specification
MCP provides a standardized way for applications to:
* Share contextual information with language models
* Expose tools and capabilities to AI systems
* Build composable integrations and workflows
The protocol uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 messages to establish
communication between:
* **Hosts**: LLM applications that initiate connections
* **Clients**: Connectors within the host application
* **Servers**: Services that provide context and capabilities
MCP takes some inspiration from the
[Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which
standardizes how to add support for programming languages across a whole ecosystem of
development tools. In a similar way, MCP standardizes how to integrate additional context
and tools into the ecosystem of AI applications.
## [​](#key-details)Key Details
### [​](#base-protocol)Base Protocol
* [JSON-RPC](https://www.jsonrpc.org/) message format
* Stateful connections
* Server and client capability negotiation
### [​](#features)Features
Servers offer any of the following features to clients:
* **Resources**: Context and data, for the user or the AI model to use
* **Prompts**: Templated messages and workflows for users
* **Tools**: Functions for the AI model to execute
Clients may offer the following features to servers:
* **Sampling**: Server-initiated agentic behaviors and recursive LLM interactions
* **Roots**: Server-initiated inquiries into URI or filesystem boundaries to operate in
* **Elicitation**: Server-initiated requests for additional information from users
### [​](#additional-utilities)Additional Utilities
* Configuration
* Progress tracking
* Cancellation
* Error reporting
* Logging
## [​](#security-and-trust-&-safety)Security and Trust & Safety
The Model Context Protocol enables powerful capabilities through arbitrary data access
and code execution paths. With this power comes important security and trust
considerations that all implementors must carefully address.
### [​](#key-principles)Key Principles
**User Consent and Control**
Users must explicitly consent to and understand all data access and operations
* Users must retain control over what data is shared and what actions are taken
* Implementors should provide clear UIs for reviewing and authorizing activities
**Data Privacy**
Hosts must obtain explicit user consent before exposing user data to servers
* Hosts must not transmit resource data elsewhere without user consent
* User data should be protected with appropriate access controls
**Tool Safety**
Tools represent arbitrary code execution and must be treated with appropriate
caution.
In particular, descriptions of tool behavior such as annotations should be
considered untrusted, unless obtained from a trusted server.
* Hosts must obtain explicit user consent before invoking any tool
* Users should understand what each tool does before authorizing its use
**LLM Sampling Controls**
Users must explicitly approve any LLM sampling requests
* Users should control:
Whether sampling occurs at all
* The actual prompt that will be sent
* What results the server can see
* The protocol intentionally limits server visibility into prompts
### [​](#implementation-guidelines)Implementation Guidelines
While MCP itself cannot enforce these security principles at the protocol level,
implementors **SHOULD**:
* Build robust consent and authorization flows into their applications
* Provide clear documentation of security implications
* Implement appropriate access controls and data protections
* Follow security best practices in their integrations
* Consider privacy implications in their feature designs
## [​](#learn-more)Learn More
Explore the detailed specification for each protocol component:
svg]:size-6" data-component-part="card-icon">## Architecture
svg]:size-6" data-component-part="card-icon">## Base Protocol
svg]:size-6" data-component-part="card-icon">## Server Features
svg]:size-6" data-component-part="card-icon">## Client Features
svg]:size-6" data-component-part="card-icon">## Contributing
Was this page helpful?
YesNo[Key Changes](/specification/2025-11-25/changelog)⌘I[github](https://github.com/modelcontextprotocol)