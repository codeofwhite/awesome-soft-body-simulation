# Contributing Guidelines / 贡献指南

Thank you for your interest in contributing! 🎉

## Scope / 范围

This list focuses **only** on deformable / soft body simulation:

- Physics engines and simulators for deformable bodies
- Cloth and garment simulation
- Differentiable simulation for deformable objects
- Benchmarks and environments for deformable manipulation
- Learning-based methods for deformable objects
- Physics-based 3D asset generation (deformable / soft)

**Out of scope:** dexterous manipulation, tactile sensing, rigid-body-only work, general robotics.

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

| Section | Description |
|---------|-------------|
| `simulators` | Physics engines and simulation platforms |
| `cloth` | Cloth and garment specific simulation |
| `differentiable` | Differentiable simulation for deformable objects |
| `benchmarks` | Standardized evaluation environments and datasets |
| `learning` | Learning-based methods for deformable manipulation |
| `generation` | Physics-based 3D asset generation |

## Quality Criteria / 质量标准

- Resources must be **relevant** to soft body / deformable object simulation
- Papers should be **published** (conference, journal, or reputable preprint)
- Tools should be **open source** or publicly available
- Each entry should have a **working URL**
- Please provide **both English and Chinese descriptions** (`desc_en` and `desc_zh`)

## Questions? / 有问题？

Open an issue if you have any questions!
有问题请提 issue！
