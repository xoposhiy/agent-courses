# FastMCP Bearer Client Authentication

[Course index](../../README.md) · [Original source](https://gofastmcp.com/clients/auth/bearer) · [Raw file](../../raw/optional-readings/ref-b614d75dfff9.html)

Retrieved: 2026-11-13T16:55:08.446113+00:00

Authentication

# Bearer Token Authentication

Copy pageCopy page

Authenticate your FastMCP client with a Bearer token.

Copy pageCopy page

New in version `2.6.0`

Bearer Token authentication is only relevant for HTTP-based transports.

You can configure your FastMCP client to use **bearer authentication** by supplying a valid access token. This is most appropriate for service accounts, long-lived API keys, CI/CD, applications where authentication is managed separately, or other non-interactive authentication methods.
A Bearer token is a JSON Web Token (JWT) that is used to authenticate a request. It is most commonly used in the `Authorization` header of an HTTP request, using the `Bearer` scheme:

```
Authorization: Bearer <token>
```

## Client Usage

The most straightforward way to use a pre-existing Bearer token is to provide it as a string to the `auth` parameter of the `fastmcp.Client` or transport instance. FastMCP will automatically format it correctly for the `Authorization` header and bearer scheme.

If you’re using a string token, do not include the `Bearer` prefix. FastMCP will add it for you.

```
from fastmcp import Client

async with Client(
    "https://your-server.fastmcp.app/mcp", 
    auth="<your-token>",
) as client:
    await client.list_tools()
```

You can also supply a Bearer token to a transport instance, such as `StreamableHttpTransport` or `SSETransport`:

```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(
    "http://your-server.fastmcp.app/mcp", 
    auth="<your-token>",
)

async with Client(transport) as client:
    await client.list_tools()
```

## `BearerAuth` Helper

If you prefer to be more explicit and not rely on FastMCP to transform your string token, you can use the `BearerAuth` class yourself, which implements the `httpx2.Auth` interface.

```
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

async with Client(
    "https://your-server.fastmcp.app/mcp", 
    auth=BearerAuth(token="<your-token>"),
) as client:
    await client.list_tools()
```

## Custom Headers

If the MCP server expects a custom header or token scheme, you can manually set the client’s `headers` instead of using the `auth` parameter by setting them on your transport:

```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async with Client(
    transport=StreamableHttpTransport(
        "https://your-server.fastmcp.app/mcp", 
        headers={"X-API-Key": "<your-token>"},
    ),
) as client:
    await client.list_tools()
```

⌘I
