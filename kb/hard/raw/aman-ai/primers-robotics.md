# Primers • Robotics

**Source:** https://aman.ai/primers/ai/robotics/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Simulation and Human Mocap](#simulation-and-human-mocap)
* [Synthetic data using Teleop](#synthetic-data-using-teleop)
* [HOVER](#hover)
* [Citation](#citation)

## Simulation and Human Mocap

Let’s reverse engineer this demo. You need 3 things: (1) robust hardware and motor designs that treat simulation as first-class citizen; (2) a human motion capture (“mocap”) dataset, such as those for film and gaming characters; (3) massively parallel RL training in GPU-accelerated simulation.

Last October, our team trained a 1.5M parameter foundation model called HOVER for such agile motor control. It follows this recipe, roughly speaking:

(1) Simulation used to be an after-thought. Now, it has to be part of the hardware design process. If your robot doesn’t simulate well, you can kiss RL goodbye. Hardware-simulation co-design is a very interesting emergent topic that only becomes meaningful with today’s compute capability.

(2) Human mocap dataset to produce natural-looking walking and running gaits. That’s one huge advantage of using humanoid robot - you get to imitate from tons of human motions that were originally captured for movies or AAA games. At least 3 ways to use the data:

* For initialization: pre-train the neural net to imitate human, and then finetune it into the robot form factor with physics turned on;
* For reward function: penalize any deviations from the target pose;
* For representation learning: treat the human poses as a “motion prior” to constrain the space of robot behaviors.

(3) Shove the above into Isaac sim, add a lot of randomization, pump it through PPO, throw in a bunch of GPUs, and then watch Netflix till loss converges.

If you have an urge to comment this is CGI, let me save you a few keystrokes — many academic labs now own the G1 robot in the flesh.

Read about our team’s HOVER work: https://lnkd.in/gfKW9K5U

## Synthetic data using Teleop

Robotics has a data scarcity problem - you simply can’t scrape robot control data from webpages. Introducing GR00T-Mimic and GR00T-Gen: using both Graphics 1.0 & Graphics 2.0 to multiply your robot datasets by 1,000,000x.

We trade compute for synthetic data, so we are not capped by the fundamental physical limit of 24 hrs/robot/day.

Robotics is right in the thick of Moravec’s paradox: things that are easy for humans turn out to be incredibly hard for machines. We are crushing the Moravec’s paradox, one token at a time.

> Graphics 1.0: Isaac simulators with manually written, GPU-accelerated physics and rendering equations.
> Graphics 2.0: big neural nets (Cosmos) that repaint the pixels from sim textures to real, given an open-ended prompt.

Robot data multiplier workflow:

1. GR00T-Teleop: use XR device like Apple Vision Pro to map human finger poses to humanoid hands.
2. GR00T-Mimic: given a human-collected task demonstration, we augment the actions in Isaac and filter out ones that fail the task.
3. GR00T-Gen: apply Graphics 1.0 and then Graphics 2.0 to produce tons of visual variations.

The above is an exponential pipeline, adding orders of magnitude at each step.

## HOVER

Not every foundation model needs to be gigantic. We trained a 1.5M-parameter neural network to control the body of a humanoid robot. It takes a lot of subconscious processing for us humans to walk, maintain balance, and maneuver our arms and legs into desired positions. We capture this “subconsciousness” in HOVER, a single model that learns how to coordinate the motors of a humanoid robot to support locomotion and manipulation.

We trained HOVER in NVIDIA Isaac, a GPU-powered simulation suite that accelerates physics by 10,000x faster than real time. To put the number in perspective, the robots undergo 1 year of intense training in a virtual “dojo”, but take only ~50 minutes of wall clock time on one GPU card. The neural net then transfers zero-shot to the real world without finetuning.

HOVER can be *prompted* for various types of high-level motion instructions that we call “control modes”. To name a few:

* Head and hand poses - can be captured by XR devices like Apple Vision Pro.
* Whole-body poses - via MoCap or RGB camera.
* Whole-body joint angles - Exoskeleton.
* Root velocity command - Joysticks.

What HOVER enables:

* A unified interface for us to control the robot using whichever input devices are convenient at hand.
* An easier way to collect whole-body teleoperation data for training.
* An upstream Vision-Language-Action model to provide motion instructions, which HOVER translates to low-level motor signals at high frequency.

HOVER supports any humanoid that can be simulated in Isaac. Bring your own robot, and watch it come to life!

It’s a big teamwork from NVIDIA GEAR Lab and collaborators: Tairan He, Wenli Xiao, Toru Lin, Zhengyi Luo, Zhenjia Xu, Zhenyu Jiang, Jan Kautz, Changliu Liu, Guanya Shi, Xiaolong Wang

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledLLMVLMBenchmarks,
  title   = {LLM/VLM Benchmarks},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
