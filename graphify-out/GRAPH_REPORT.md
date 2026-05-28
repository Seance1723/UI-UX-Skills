# Graph Report - .  (2026-05-28)

## Corpus Check
- 74 files · ~74,362 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 132 nodes · 221 edges · 9 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]

## God Nodes (most connected - your core abstractions)
1. `fail()` - 13 edges
2. `main()` - 12 edges
3. `handle()` - 10 edges
4. `handle()` - 10 edges
5. `callTool()` - 8 edges
6. `callTool()` - 8 edges
7. `installProject()` - 6 edges
8. `installProject()` - 6 edges
9. `writeFile()` - 5 edges
10. `copyProjectSkillAssets()` - 5 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (9 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.16
Nodes (21): assetMap, callTool(), err(), __filename, getPrompt(), handle(), installInstructions(), jsonText() (+13 more)

### Community 1 - "Community 1"
Cohesion: 0.16
Nodes (21): assetMap, callTool(), err(), __filename, getPrompt(), handle(), installInstructions(), jsonText() (+13 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (19): agents, bin, cjs, dir, __dirname, doctor, __filename, help (+11 more)

### Community 3 - "Community 3"
Cohesion: 0.2
Nodes (16): appendMarked(), copyDir(), copyProjectSkillAssets(), doctor(), escapeRegExp(), __filename, findProjectRoot(), installGlobal() (+8 more)

### Community 4 - "Community 4"
Cohesion: 0.2
Nodes (16): appendMarked(), copyDir(), copyProjectSkillAssets(), doctor(), escapeRegExp(), __filename, findProjectRoot(), installGlobal() (+8 more)

### Community 5 - "Community 5"
Cohesion: 0.32
Nodes (16): check_agent_templates(), check_bin_installer(), check_discovery_assets(), check_markdown_links(), check_mcp_server(), check_package_json(), check_referenced_files_exist(), check_release_artifacts() (+8 more)

### Community 6 - "Community 6"
Cohesion: 0.29
Nodes (5): assets, bins, packageRoot, _pkg, _require

## Knowledge Gaps
- **42 isolated node(s):** `packageRoot`, `_require`, `_pkg`, `bins`, `assets` (+37 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `packageRoot`, `_require`, `_pkg` to the rest of the system?**
  _42 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._