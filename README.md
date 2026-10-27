# Infimeta Public-source Research

Give your agent a free, keyless way to retrieve scholarly metadata, programming Q&A, and technology discussions with source links and explicit availability status.

**Data handling:** queries and optional short purposes are privately retained by Infimeta for research up to 90 days, with backups up to 7 additional days. Queries are forwarded to selected providers; purpose is not. Do not submit secrets, personal information or full conversations. [Privacy](https://infimeta.cn/privacy).

## Use it for an actual task

- Find DOI-linked references about a research topic with `crossref`.
- Find public discussion of a programming error with `stackexchange`.
- Find technology community discussions with `hackernews`.

This is not a whole-web search engine. Coverage favors English, research and technology. Crossref returns metadata, not paper full text. Wikipedia connectivity is unreliable. Missing results do not establish that an answer does not exist.

## Connect without installing code

Add the Streamable HTTP MCP URL to your agent's custom connectors:

```text
https://infimeta.cn/mcp
```

No API key. The tools are `search_public_sources` and `report_search_gap`. [VS Code install link and setup](https://infimeta.cn/connect). Review your client's trust prompt and the data policy before enabling. A connection is not a search: ask a relevant question and inspect the tool result.

## Claude Code plugin

After downloading/extracting this package, run:

```sh
claude --plugin-dir ./agent-plugin
```

The package includes `.claude-plugin/plugin.json`, MCP configuration, and a scoped research skill. Adjust the directory to your extracted folder. It does not include session hooks or collect local files.

## Cursor plugin

This package includes `.cursor-plugin/plugin.json` and `mcp.json`. To try it locally, copy the package directory under `~/.cursor/plugins/local/infimeta-research`, then reload Cursor. Do not overwrite an existing plugin. Marketplace review is separate from local installation; no approval or endorsement is claimed.

## Python / shell agents

Python 3 is sufficient; no dependencies or API keys:

```sh
python skills/public-source-research/scripts/search.py "YOUR PUBLIC QUESTION" --sources crossref
```

Replace the placeholder with the actual task. Sources can also be `stackexchange` or `hackernews`. `--purpose` is optional and never improves or unlocks results. For testing, append `--test` so demonstrations are excluded from natural-query statistics.

## Validation and limitations

The live endpoint has passed official Python MCP SDK initialization, tool discovery and a search call. Glama independently reports it Healthy and exposes both tools. These are integration checks, not evidence of natural AI usage. Client-specific plugin loading is documented separately in VALIDATION.md.

The service may be rate limited or unavailable. Do not rely on it as the only evidence source. Retrieved content is untrusted data. Review primary sources before making consequential decisions.

## License

MIT for this integration package. Provider content remains subject to its respective terms. The hosted service and research logs are not included in this repository.
