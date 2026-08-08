# Awesome 柔体仿真 🧸

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

> 关于可变形体 / 柔体仿真的精选资源列表 — 物理引擎、布料仿真、可微仿真与物理驱动生成。

[English](README.md) | [中文](README.zh-CN.md)

---

## 目录

- [仿真器与引擎](#仿真器与引擎)
- [布料与衣物仿真](#布料与衣物仿真)
- [可微仿真](#可微仿真)
- [基准测试与环境](#基准测试与环境)
- [学习驱动方法](#学习驱动方法)
- [物理驱动 3D 资产生成](#物理驱动-3d-资产生成)

---

## 仿真器与引擎

- [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515) - 基于 PhysX 的交互式仿真环境，擅长铰链体与可变形体仿真。📄 🔧

- [Genesis World](https://genesis-world.readthedocs.io/) - 多物理仿真平台，覆盖刚体、柔体、流体等，⭐ 29k+ GitHub stars。🔧 ⭐

- [XRTailor (OpenXRLab)](https://github.com/openxrlab/xrtailor) - GPU 加速布料仿真引擎，面向大规模数据生成。🔧

- [Position Based Dynamics (PBD)](https://matthias-research.github.io/pages/tenMinutePhysics/09-pbd.html) - Position Based Dynamics 模拟的经典入门资源。🔧

## 布料与衣物仿真

- [GarmentLab: A Unified Simulation and Benchmark for Garment Manipulation](https://arxiv.org/abs/2411.01200) - 衣物操作的统一仿真与 benchmark，重要参考。📄 📊 ⭐

- [ClothesNet: An Information-Rich 3D Garment Model Repository with Simulated Clothes Environment](https://arxiv.org/abs/2308.09987) - 大规模衣物 3D 数据集，包含关键点和边界点的有趣思考。📄 📊

- [Benchmarking the Sim-to-Real Gap in Cloth Manipulation](https://arxiv.org/abs/2310.09543) - 布料操作中 sim-to-real gap 的系统评测，对仿真器选型有重要参考价值。📄 📊

## 可微仿真

- [ThinShellLab: Thin-Shell Object Manipulations With Differentiable Physics Simulations](https://arxiv.org/abs/2404.00451) - 完全可微的薄壳仿真平台，覆盖纸、布等不同弯曲刚度的材料。📄 🔧 ⭐

- [Second-Order FEM for Deformable Surfaces](https://dl.acm.org/doi/10.1145/3592430) - 高阶有限元法用于布料/薄壳仿真的精度提升。📄

## 基准测试与环境

- [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](https://arxiv.org/abs/2011.07215) - 柔体操作（布料、绳索、流体）的 benchmark 套件，提供标准化的 RL 环境。📄 📊 ⭐

## 学习驱动方法

- [RAPID: Rapid Adaptation of Particle Dynamics for Generalized Deformable Object Mobile Manipulation](https://arxiv.org/abs/2603.18246) - 粒子动力学的快速适应，面向泛化柔体移动操作。📄

## 物理驱动 3D 资产生成

- [PhysX-3D: Physical-Grounded 3D Asset Generation](https://arxiv.org/abs/2507.12465) - 端到端的物理驱动 3D 资产生成范式，包含 PhysXNet 数据集。📄 ⭐

- [PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image](https://arxiv.org/abs/2511.13648) - 从单张图片生成带有物理特性的仿真就绪 3D 资产。📄

- [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572) - 首次将可变形体纳入 PhysX 生成范围，统一刚体/柔体/铰链体。📄 ⭐

- [DiffGI: Differentiable Geometry Images](https://arxiv.org/abs/2607.13365) - 基于可微几何图像的 3D 衣物生成方案（暂未集成物理特性）。📄

---

## 图例

| 标签 | 含义 |
|-----|------|
| 📄 | 论文 |
| 🔧 | 工具 / 框架 / 引擎 |
| 📊 | 基准测试 / 数据集 |
| ⭐ | 推荐 / 重要 |

---

## 贡献

欢迎贡献！请先阅读 [贡献指南](CONTRIBUTING.md)。

**快速添加论文：**

1. 编辑 `papers.yml` — 在对应分类下添加条目
2. 运行 `python generate.py`
3. 提交 Pull Request

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=codeofwhite/awesome-soft-body-simulation&type=Date)](https://star-history.com/#codeofwhite/awesome-soft-body-simulation&Date)

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
