# AWS Labs Timestream for InfluxDB MCP Server

An AWS Labs Model Context Protocol (MCP) server for Timestream for InfluxDB. This server provides tools to interact with AWS Timestream for InfluxDB APIs, allowing you to create and manage database instances, clusters, parameter groups, and more. It also includes tools to interact with InfluxDB's write and query APIs.

## Features

- Create, update, list, describe, and delete Timestream for InfluxDB database instances
- Create, update, list, describe, and delete Timestream for InfluxDB database clusters
- Manage DB parameter groups
- Tag management for Timestream for InfluxDB resources
- Write and query data using InfluxDB's APIs


## Pre-requisites
1. Install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/) or the [GitHub README](https://github.com/astral-sh/uv#installation)
2. Install Python using `uv python install 3.10`
3. Set up AWS credentials with access to AWS services
    - You need an AWS account with appropriate permissions
    - Configure AWS credentials with `aws configure` or environment variables
    - Consider starting with Read-only permission if you don't want the LLM to modify any resources

## Installation

| Cursor | VS Code |
|:------:|:-------:|
| [![Install MCP Server](https://cursor.com/deeplink/mcp-install-light.svg)](https://cursor.com/install-mcp?name=awslabs.timestream-for-influxdb-mcp-server&config=eyJjb21tYW5kIjoidXZ4IGF3c2xhYnMudGltZXN0cmVhbS1mb3ItaW5mbHV4ZGItbWNwLXNlcnZlckBsYXRlc3QiLCJlbnYiOnsiQVdTX1BST0ZJTEUiOiJ5b3VyLWF3cy1wcm9maWxlIiwiQVdTX1JFR0lPTiI6InVzLWVhc3QtMSIsIkZBU1RNQ1BfTE9HX0xFVkVMIjoiRVJST1IifSwiZGlzYWJsZWQiOmZhbHNlLCJhdXRvQXBwcm92ZSI6W119) | [![Install on VS Code](https://img.shields.io/badge/Install_on-VS_Code-FF9900?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Timestream%20for%20InfluxDB%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.timestream-for-influxdb-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22AWS_PROFILE%22%3A%22your-aws-profile%22%2C%22AWS_REGION%22%3A%22us-east-1%22%2C%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D) |

You can modify the settings of your MCP client to run your local server (e.g. for Amazon Q Developer CLI MCP, `~/.aws/amazonq/mcp.json`)

```json
{
  "mcpServers": {
    "awslabs.timestream-for-influxdb-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.timestream-for-influxdb-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### Available Tools

The Timestream for InfluxDB MCP server provides the following tools:

#### AWS Timestream for InfluxDB Management

##### Database Cluster Management
- `CreateDbCluster`: Create a new Timestream for InfluxDB database cluster
- `GetDbCluster`: Retrieve information about a specific DB cluster
- `DeleteDbCluster`: Delete a Timestream for InfluxDB database cluster
- `ListDbClusters`: List all Timestream for InfluxDB database clusters
- `UpdateDbCluster`: Update a Timestream for InfluxDB database cluster
- `ListDbClusters`: List all Timestream for InfluxDB database clusters
- `ListDbInstancesForCluster`: List DB instances belonging to a specific cluster
- `ListClustersByStatus`: List DB clusters filtered by status

##### Database Instance Management
- `CreateDbInstance`: Create a new Timestream for InfluxDB database instance
- `GetDbInstance`: Retrieve information about a specific DB instance
- `DeleteDbInstance`: Delete a Timestream for InfluxDB database instance
- `ListDbInstances`: List all Timestream for InfluxDB database instances
- `UpdateDbInstance`: Update a Timestream for InfluxDB database instance
- `ListDbInstancesByStatus`: List DB instances filtered by status

##### Parameter Group Management
- `CreateDbParamGroup`: Create a new DB parameter group
- `GetDbParameterGroup`: Retrieve information about a specific DB parameter group
- `ListDbParamGroups`: List all DB parameter groups

##### Tag Management
- `ListTagsForResource`: List all tags on a Timestream for InfluxDB resource
- `TagResource`: Add tags to a Timestream for InfluxDB resource
- `UntagResource`: Remove tags from a Timestream for InfluxDB resource

#### InfluxDB Data Operations

##### Write API
- `InfluxDBWritePoints`: Write data points to InfluxDB
- `InfluxDBWriteLP`: Write data in Line Protocol format to InfluxDB

##### Query API
- `InfluxDBQuery`: Query data from InfluxDB using Flux query language
