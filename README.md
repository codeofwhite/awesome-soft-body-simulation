# Awesome Soft Body Simulation 🧸

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

> A curated list of resources on deformable/soft body simulation, dexterous manipulation, tactile sensing, and physics-based generation.

[English](README.md) | [中文](README.zh-CN.md)

---

## Contents

- [Benchmarks & Datasets](#benchmarks--datasets)
- [Simulators & Engines](#simulators--engines)
- [Dexterous Manipulation + Deformable](#dexterous-manipulation--deformable)
- [Garment & Cloth](#garment--cloth)
- [Tactile Sensing](#tactile-sensing)
- [Physics-Based 3D Asset Generation](#physics-based-3d-asset-generation)
- [Learning for Deformable Objects](#learning-for-deformable-objects)
- [Fundamentals (PBD, FEM, etc.)](#fundamentals-pbd-fem-etc)

---

## Benchmarks & Datasets

- [DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo](https://arxiv.org/abs/2605.16257) - Task-oriented dexterous manipulation benchmark on MuJoCo, covering tool-use, bimanual coordination, and long-horizon execution. 📄 📊

- [SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation](https://arxiv.org/abs/2607.04234) - Safety-aware visuo-tactile benchmark focusing on physical constraints during deformable object manipulation. 📄 📊

- [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](https://arxiv.org/abs/2011.07215) - Benchmark suite for deformable object manipulation (cloth, rope, fluid) with standardized RL environments. 📄 📊 ⭐

- [Benchmarking the Sim-to-Real Gap in Cloth Manipulation](https://arxiv.org/abs/2310.09543) - Systematic evaluation of the sim-to-real gap in cloth manipulation across different simulators. 📄 📊

## Simulators & Engines

- [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515) - Interactive simulation environment based on PhysX, excelling at articulated object modeling, widely used in medical simulation. 📄 🔧

- [Genesis World](https://genesis-world.readthedocs.io/) - Multi-physics simulation platform covering rigid, deformable, and fluid bodies. 29k+ GitHub stars. 🔧 ⭐

- [XRTailor (OpenXRLab)](https://github.com/openxrlab/xrtailor) - GPU-accelerated cloth simulation engine for large-scale data generation. 🔧

## Dexterous Manipulation + Deformable

- [DexDeform: Dexterous Deformable Object Manipulation with Human Demonstrations and Differentiable Physics](https://arxiv.org/abs/2304.03223) - Dexterous hand + deformable object manipulation combining human demonstrations with differentiable physics. 📄 ⭐

- [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://arxiv.org/abs/2506.18088) - Automated large-scale data generation for bimanual manipulation, built on SAPIEN with cross-embodiment support. 📄 🔧

- [SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation](https://arxiv.org/abs/2606.08278) - MuJoCo + Isaac Sim joint solution for humanoid loco-manipulation (rigid body only). 📄

## Garment & Cloth

- [GarmentLab: A Unified Simulation and Benchmark for Garment Manipulation](https://arxiv.org/abs/2411.01200) - Unified simulation and benchmark for garment manipulation tasks. 📄 📊 ⭐

- [ClothesNet: An Information-Rich 3D Garment Model Repository with Simulated Clothes Environment](https://arxiv.org/abs/2308.09987) - Large-scale 3D garment dataset with rich annotations, including keypoints and boundary analysis. 📄 📊

## Tactile Sensing

- [UniVTAC: A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking](https://arxiv.org/abs/2602.10093) - Complete visuo-tactile data generation pipeline, supporting 3 tactile sensors and 8 manipulation tasks. 📄 🔧 ⭐

- [Neo-Zero](https://arxiv.org/search/?query=Neo-Zero&searchtype=all) - End-to-end dexterous hand + tactile + deformable manipulation based on UniVTAC simulator. 📄

## Physics-Based 3D Asset Generation

- [PhysX-3D: Physical-Grounded 3D Asset Generation](https://arxiv.org/abs/2507.12465) - End-to-end paradigm for physical-grounded 3D asset generation with PhysXNet dataset. 📄 ⭐

- [PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image](https://arxiv.org/abs/2511.13648) - Generate simulation-ready 3D assets with physical properties from a single image. 📄

- [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572) - First to include deformable objects in PhysX generation scope, unifying rigid/deformable/articulated. 📄 ⭐

- [DiffGI: Differentiable Geometry Images](https://arxiv.org/abs/2607.13365) - 3D garment generation via differentiable geometry images (no integrated physics yet). 📄

## Learning for Deformable Objects

- [RAPID: Rapid Adaptation of Particle Dynamics for Generalized Deformable Object Mobile Manipulation](https://arxiv.org/abs/2603.18246) - Rapid adaptation of particle dynamics for generalized deformable object mobile manipulation. 📄

## Fundamentals (PBD, FEM, etc.)

- [Position Based Dynamics (PBD)](https://matthias-research.github.io/pages/tenMinutePhysics/09-pbd.html) - Classic introductory resource for Position Based Dynamics simulation. 🔧

- [ThinShellLab: Thin-Shell Object Manipulations With Differentiable Physics Simulations](https://arxiv.org/abs/2404.00451) - Fully differentiable simulation platform for thin-shell materials (paper, cloth) with varying bending stiffness. 📄 🔧

---

## Legend

| Tag | Meaning |
|-----|---------|
| 📄 | Paper |
| 🔧 | Tool / Framework / Engine |
| 📊 | Benchmark / Dataset |
| ⭐ | Recommended / Important |

---

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

**Quick way to add a paper:**

1. Edit `papers.yml` — add your entry under the appropriate section
2. Run `python generate.py`
3. Submit a Pull Request

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=codeofwhite/awesome-soft-body-simulation&type=Date)](https://star-history.com/#codeofwhite/awesome-soft-body-simulation&Date)

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
