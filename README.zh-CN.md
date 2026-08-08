# Awesome 柔体仿真 🧸

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

> 关于柔体/可变形体仿真、灵巧操作、触觉感知和物理驱动生成的精选资源列表。

[English](README.md) | [中文](README.zh-CN.md)

---

## 目录

- [基准测试与数据集](#基准测试与数据集)
- [仿真器与引擎](#仿真器与引擎)
- [灵巧操作 + 柔体](#灵巧操作--柔体)
- [衣物与布料](#衣物与布料)
- [触觉感知](#触觉感知)
- [物理驱动 3D 资产生成](#物理驱动-3d-资产生成)
- [柔体学习方法](#柔体学习方法)
- [基础理论（PBD、FEM 等）](#基础理论pbdfem-等)

---

## 基准测试与数据集

- [DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo](https://arxiv.org/abs/2605.16257) - MuJoCo 上的任务导向灵巧操作 benchmark，覆盖工具使用、双臂协调和长时序执行。📄 📊

- [SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation](https://arxiv.org/abs/2607.04234) - 面向过程安全的视觉-触觉 benchmark，关注柔体操作中的物理约束。📄 📊

- [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](https://arxiv.org/abs/2011.07215) - 柔体操作（布料、绳索、流体）的 benchmark 套件，提供标准化的 RL 环境。📄 📊 ⭐

- [Benchmarking the Sim-to-Real Gap in Cloth Manipulation](https://arxiv.org/abs/2310.09543) - 布料操作中 sim-to-real gap 的系统评测，对仿真器选型有重要参考价值。📄 📊

## 仿真器与引擎

- [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515) - 基于 PhysX 的交互式仿真环境，擅长铰链物体建模，广泛用于医学仿真。📄 🔧

- [Genesis World](https://genesis-world.readthedocs.io/) - 多物理仿真平台，覆盖刚体、柔体、流体等，⭐ 29k+ GitHub stars。🔧 ⭐

- [XRTailor (OpenXRLab)](https://github.com/openxrlab/xrtailor) - GPU 加速布料仿真引擎，面向大规模数据生成。🔧

## 灵巧操作 + 柔体

- [DexDeform: Dexterous Deformable Object Manipulation with Human Demonstrations and Differentiable Physics](https://arxiv.org/abs/2304.03223) - 灵巧手 + 柔体操作，结合人类示教与可微物理。📄 ⭐

- [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://arxiv.org/abs/2506.18088) - 自动化大规模双臂操作数据生成，基于 SAPIEN，支持跨本体。📄 🔧

- [SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation](https://arxiv.org/abs/2606.08278) - MuJoCo + Isaac Sim 联合方案，解决人形机器人的移动操作（仅刚体）。📄

## 衣物与布料

- [GarmentLab: A Unified Simulation and Benchmark for Garment Manipulation](https://arxiv.org/abs/2411.01200) - 衣物操作的统一仿真与 benchmark，重要参考。📄 📊 ⭐

- [ClothesNet: An Information-Rich 3D Garment Model Repository with Simulated Clothes Environment](https://arxiv.org/abs/2308.09987) - 大规模衣物 3D 数据集，包含关键点和边界点的有趣思考。📄 📊

## 触觉感知

- [UniVTAC: A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking](https://arxiv.org/abs/2602.10093) - 完整的视觉-触觉数据生成 pipeline，支持 3 种触觉传感器和 8 个操作任务。📄 🔧 ⭐

- [Neo-Zero](https://arxiv.org/search/?query=Neo-Zero&searchtype=all) - 基于 UniVTAC 仿真器的灵巧手 + 触觉 + 柔体端到端方案。📄

## 物理驱动 3D 资产生成

- [PhysX-3D: Physical-Grounded 3D Asset Generation](https://arxiv.org/abs/2507.12465) - 端到端的物理驱动 3D 资产生成范式，包含 PhysXNet 数据集。📄 ⭐

- [PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image](https://arxiv.org/abs/2511.13648) - 从单张图片生成带有物理特性的仿真就绪 3D 资产。📄

- [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572) - 首次将可变形体纳入 PhysX 生成范围，统一刚体/柔体/铰链体。📄 ⭐

- [DiffGI: Differentiable Geometry Images](https://arxiv.org/abs/2607.13365) - 基于可微几何图像的 3D 衣物生成方案（暂未集成物理特性）。📄

## 柔体学习方法

- [RAPID: Rapid Adaptation of Particle Dynamics for Generalized Deformable Object Mobile Manipulation](https://arxiv.org/abs/2603.18246) - 粒子动力学的快速适应，面向泛化柔体移动操作。📄

## 基础理论（PBD、FEM 等）

- [Position Based Dynamics (PBD)](https://matthias-research.github.io/pages/tenMinutePhysics/09-pbd.html) - Position Based Dynamics 模拟的经典入门资源。🔧

- [ThinShellLab: Thin-Shell Object Manipulations With Differentiable Physics Simulations](https://arxiv.org/abs/2404.00451) - 完全可微的薄壳仿真平台，覆盖纸、布等不同弯曲刚度的材料。📄 🔧

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
