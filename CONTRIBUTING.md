# Contributing Guidelines / 贡献指南

Thank you for your interest in contributing! 🎉

## How to Add a Paper / 如何添加论文

**Edit one file, run one command:**

1. Open `papers.yml`
2. Add your entry under the appropriate section:

```yaml
- title: "Your Paper Title"
  url: "https://arxiv.org/abs/xxxx.xxxxx"
  venue: "ICRA"          # optional
  year: 2026             # optional
  tags: [paper, star]    # paper / tool / dataset / benchmark / star
  desc_en: "One-line English description."
  desc_zh: "一行中文描述。"
```

3. Run `python generate.py` (requires `pip install pyyaml`)
4. This auto-generates both `README.md` (EN) and `README.zh-CN.md` (CN)
5. Submit a Pull Request

## Tags / 标签

| Tag | Meaning | 含义 |
|-----|---------|------|
| 📄 `paper` | Research paper | 论文 |
| 🔧 `tool` | Tool / Framework / Engine | 工具 / 框架 / 引擎 |
| 📊 `dataset` | Dataset | 数据集 |
| 📊 `benchmark` | Benchmark | 基准测试 |
| ⭐ `star` | Recommended / Important | 推荐 / 重要 |

## Sections / 分类

Place your entry in the most relevant section:

| Section | Description |
|---------|-------------|
| `benchmarks` | Standardized evaluation environments and datasets |
| `simulators` | Simulation platforms and physics engines |
| `dexterous` | Dexterous hand + deformable objects |
| `garment` | Cloth/garment specific work |
| `tactile` | Tactile sensing for manipulation |
| `generation` | Generating 3D assets with physical properties |
| `learning` | Learning-based methods for deformable manipulation |
| `fundamentals` | Core algorithms (PBD, FEM, MPM, etc.) |

## Quality Criteria / 质量标准

- Resources should be **relevant** to soft body / deformable object simulation
- Papers should be **published** (conference, journal, or reputable preprint)
- Tools should be **open source** or publicly available
- Each entry should have a **working URL**
- Please provide **both English and Chinese descriptions** (`desc_en` and `desc_zh`)

## Questions? / 有问题？

Open an issue if you have any questions!
有问题请提 issue！
