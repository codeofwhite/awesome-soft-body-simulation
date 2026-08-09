#!/usr/bin/env python3
"""
Generate README.md (English) and README.zh-CN.md (Chinese) from papers.yml.

Usage:
    pip install pyyaml
    python generate.py
"""

import re
import yaml
from pathlib import Path

TAG_EMOJI = {
    "paper": "📄",
    "tool": "🔧",
    "dataset": "📊",
    "benchmark": "📊",
    "star": "⭐",
}


def github_anchor(heading: str) -> str:
    """Convert a markdown heading to a GitHub-compatible anchor link."""
    anchor = heading.lower()
    # Remove characters that are not alphanumeric, space, or hyphen
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    # Replace spaces with hyphens
    anchor = re.sub(r"\s+", "-", anchor)
    # Collapse multiple hyphens
    anchor = re.sub(r"-+", "-", anchor)
    # Remove leading/trailing hyphens
    anchor = anchor.strip("-")
    return anchor


def render_entry(paper: dict, lang: str) -> str:
    """Render a single paper entry as a markdown list item."""
    title = paper["title"]
    url = paper["url"]
    tags = " ".join(TAG_EMOJI.get(t, "") for t in paper.get("tags", []))
    desc = paper.get(f"desc_{lang}", "")

    parts = [f"- [{title}]({url})"]
    if desc:
        parts.append(f" - {desc}")
    if tags:
        parts.append(f" {tags}")
    return "".join(parts)


def render_section(section: dict, lang: str) -> str:
    """Render a full section with heading and entries."""
    title = section[f"title_{lang}"]
    lines = [f"## {title}", ""]
    for paper in section["papers"]:
        lines.append(render_entry(paper, lang))
    lines.append("")
    return "\n".join(lines)


def generate(data: dict, lang: str, output_path: Path):
    """Generate a full README file."""
    meta = data["meta"]
    title = meta[f"title_{lang}"]
    desc = meta[f"description_{lang}"]

    lines = [
        f"# {title} 🧸",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)",
        "",
        f"> {desc}",
        "",
        "[English](README.md) | [中文](README.zh-CN.md)",
        "",
        "---",
        "",
    ]

    # Table of Contents
    toc_label = "Contents" if lang == "en" else "目录"
    lines.append(f"## {toc_label}")
    lines.append("")
    for section in data["sections"]:
        stitle = section[f"title_{lang}"]
        anchor = github_anchor(stitle)
        lines.append(f"- [{stitle}](#{anchor})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sections
    for section in data["sections"]:
        lines.append(render_section(section, lang))

    # Legend
    legend_title = "Legend" if lang == "en" else "图例"
    tag_header = "Tag" if lang == "en" else "标签"
    meaning_header = "Meaning" if lang == "en" else "含义"

    legend_descriptions = {
        "en": {
            "paper": "Paper",
            "tool": "Tool / Framework / Engine",
            "dataset": "Benchmark / Dataset",
            "star": "Recommended / Important",
        },
        "zh": {
            "paper": "论文",
            "tool": "工具 / 框架 / 引擎",
            "dataset": "基准测试 / 数据集",
            "star": "推荐 / 重要",
        },
    }

    lines.extend([
        "---",
        "",
        f"## {legend_title}",
        "",
        f"| {tag_header} | {meaning_header} |",
        "|-----|---------|",
    ])
    seen_emojis = set()
    for tag, emoji in TAG_EMOJI.items():
        if emoji in seen_emojis:
            continue
        seen_emojis.add(emoji)
        desc_text = legend_descriptions[lang].get(tag, tag)
        lines.append(f"| {emoji} | {desc_text} |")
    lines.append("")

    # Contributing
    if lang == "en":
        lines.extend([
            "---",
            "",
            "## Contributing",
            "",
            "Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.",
            "",
            "**Quick way to add a paper:**",
            "",
            "1. Edit `papers.yml` — add your entry under the appropriate section",
            "2. Run `python generate.py`",
            "3. Submit a Pull Request",
            "",
            "---",
            "",
            "## License",
            "",
            "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)",
        ])
    else:
        lines.extend([
            "---",
            "",
            "## 贡献",
            "",
            "欢迎贡献！请先阅读 [贡献指南](CONTRIBUTING.md)。",
            "",
            "**快速添加论文：**",
            "",
            "1. 编辑 `papers.yml` — 在对应分类下添加条目",
            "2. 运行 `python generate.py`",
            "3. 提交 Pull Request",
            "",
            "---",
            "",
            "## 许可证",
            "",
            "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)",
        ])

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated: {output_path}")


def main():
    root = Path(__file__).parent
    with open(root / "papers.yml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    generate(data, "en", root / "README.md")
    generate(data, "zh", root / "README.zh-CN.md")
    print("Done!")


if __name__ == "__main__":
    main()
