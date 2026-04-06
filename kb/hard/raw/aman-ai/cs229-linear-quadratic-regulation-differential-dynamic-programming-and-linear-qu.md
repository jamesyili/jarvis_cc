# CS229 • Linear Quadratic Regulation, Differential Dynamic Programming and Linear Quadratic Gaussian

**Source:** https://aman.ai/cs229/lqr-ddp-lqg/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-theory

---

* [Finite-horizon MDPs](#finite-horizon-mdps)
  + [Theorem](#theorem)
* [Linear Quadratic Regulation (LQR)](#linear-quadratic-regulation-lqr)
* [From non-linear dynamics to LQR](#from-non-linear-dynamics-to-lqr)
  + [Linearization of dynamics](#linearization-of-dynamics)
  + [Differential Dynamic Programming (DDP)](#differential-dynamic-programming-ddp)
* [Linear Quadratic Gaussian (LQG)](#linear-quadratic-gaussian-lqg)
* [References](#references)
* [Citation](#citation)

## Finite-horizon MDPs

* In our discussion on [reinforcement learning](../rl), we defined Markov Decision Processes (MDPs) and covered Value Iteration/Policy Iteration in a simplified setting. More specifically we introduced the optimal Bellman equation that defines the optimal value function \(V^{\pi^{\ast}}\) of the optimal policy \(\pi^{\ast}\),

\[V^{\pi^{\ast}}(s)=R(s)+\max \_{a \in \mathcal{A}} \gamma \sum\_{s^{\prime} \in S} P\_{s a}\left(s^{\prime}\right) V^{\pi^{\ast}}\left(s^{\prime}\right)\]

* Recall that from the optimal value function, we were able to recover the optimal policy \(\pi^{\ast}\) with,

\[\pi^{\ast}(s)=\operatorname\*{arg\,max}\_{a \in \mathcal{A}} \sum\_{s^{\prime} \in \mathcal{S}} P\_{s a}\left(s^{\prime}\right) V^{\ast}\left(s^{\prime}\right)\]

* In this topic, we’ll place ourselves in a more general setting:

  1. We want to write equations that make sense for both the discrete and the continuous case. We’ll therefore write,

     \[\mathbb{E}\_{s^{\prime} \sim P\_{s a}}\left[V^{\pi^{\ast}}\left(s^{\prime}\right)\right] \quad \text { instead of } \sum\_{s^{\prime} \in S} P\_{s a}\left(s^{\prime}\right) V^{\pi^{\ast}}\left(s^{\prime}\right)\]
     + meaning that we take the expectation of the value function at the next state. In the finite case, we can rewrite the expectation as a sum over states. In the continuous case, we can rewrite the expectation as an integral. The notation \(s^{\prime} \sim p\_{s a}\) means that the state \(s^{\prime}\) is sampled from the distribution \(p\_{s a}\).
  2. We’ll assume that the rewards depend on both states and actions. In other words, \(R: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}\). This implies that the previous mechanism for computing the optimal action is changed into,

     \[\pi^{\ast}(s)=\operatorname\*{arg\,max}\_{a \in \mathcal{A}} R(s, a)+\gamma \mathbb{E}\_{s^{\prime} \sim P\_{s a}}\left[V^{\pi^{\ast}}\left(s^{\prime}\right)\right]\]
  3. Instead of considering an infinite horizon MDP, we’ll assume that we have a finite horizon MDP that will be defined as a tuple,

     \[\left(\mathcal{S}, \mathcal{A}, P\_{s a}, T, R\right)\]
     + with \(T>0\) the time horizon (for instance \(T=100\)). In this setting, our definition of payoff is going to be (slightly) different:

       \[R\left(s\_{0}, a\_{0}\right)+R\left(s\_{1}, a\_{1}\right)+\cdots+R\left(s\_{T}, a\_{T}\right)\]
     + instead of (the infinite horizon case),

       \[\begin{array}{l}
       R\left(s\_{0}, a\_{0}\right)+\gamma R\left(s\_{1}, a\_{1}\right)+\gamma^2 R\left(s\_2, a\_2\right)+\ldots \\
       \sum\_{t=0}^{\infty} R\left(s\_{t}, a\_{t}\right) \gamma^{t}
       \end{array}\]
     + What happened to the discount factor \(\gamma\)? Remember that the introduction of \(\gamma\) was (partly) justified by the necessity of making sure that the infinite sum would be finite and well-defined. If the rewards are bounded by a constant \(\bar{R}\), the payoff is indeed bounded by,

       \[\left|\sum\_{t=0}^{\infty} R\left(s\_{t}\right) \gamma^{t}\right| \leq \bar{R} \sum\_{t=0}^{\infty} \gamma^{t}\]
     + and we recognize a geometric sum! Here, as the payoff is a finite sum, the discount factor \(\gamma\) is not necessary anymore.
     + In this new setting, things behave quite differently. First, the optimal policy \(\pi^{\ast}\) might be non-stationary, meaning that it changes over time. In other words, now we have,

       \[\pi^{(t)}: \mathcal{S} \rightarrow \mathcal{A}\]
       - where the superscript \((t)\) denotes the policy at time step \(t\). The dynamics of the finite horizon MDP following policy \(\pi^{(t)}\) proceeds as follows:
         we start in some state \(s\_{0}\), take some action \(a\_{0}:=\pi^{(0)}\left(s\_{0}\right)\) according to our policy at time step 0. The MDP transitions to a successor \(s\_{1}\), drawn according to \(p\_{s\_{0} a\_{0}}\). Then, we get to pick another action \(a\_{1}:=\pi^{(1)}\left(s\_{1}\right)\) following our new policy at time step 1 and so on.
     + So, the question is: Why does the optimal policy happen to be non-stationary in the finite horizon setting? Intuitively, as we have a finite numbers of actions to take, we might want to adopt different strategies depending on where we are in the environment and how much time we have left. Imagine a grid with 2 goals with rewards \(+1\) and \(+10\). At the beginning, we might want to take actions to aim for the \(+10\) goal. But if after some steps, dynamics somehow pushed us closer to the +1 goal and we don’t have enough steps left to be able to reach the \(+10\) goal, then a better strategy would be to aim for the \(+1\) goal.
  4. This observation allows us to use time dependent dynamics,

     \[s\_{t+1} \sim p\_{s\_{t}, a\_{t}}^{(t)}\]
     + meaning that the transition’s distribution \(p\_{s\_{t}, a\_{t}}^{(t)}\) changes over time. The same thing can be said about \(R^{(t)}\). Note that this setting is a better model for real life. In a car, the gas tank empties, traffic changes, etc. Combining the previous remarks, we’ll use the following general formulation for our finite horizon MDP

       \[\left(\mathcal{S}, \mathcal{A}, p\_{s a}^{(t)}, T, R^{(t)}\right)\]
     + **Remark:** notice that the above formulation would be equivalent to adding the time into the state.
     + The value function at time \(t\) for a policy \(\pi\) is then defined in the same way as before, as an expectation over trajectories generated following policy \(\pi\) starting in state \(s\).

       \[V\_{t}(s)=\mathbb{E}\left[R^{(t)}\left(s\_{t}, a\_{t}\right)+\cdots+R^{(T)}\left(s\_{T}, a\_{T}\right) \mid s\_{t}=s, \pi\right]\]
* Now, the question is: in this finite-horizon setting, how do we find the optimal value function?

\[V\_{t}^{\ast}(s)=\max \_{\pi} V\_{t}^{\pi}(s)\]

* It turns out that Bellman’s equation for Value Iteration is made for Dynamic Programming. This may come as no surprise as Bellman is one of the fathers of dynamic programming and the Bellman equation is strongly related to the field. To understand how we can simplify the problem by adopting an iteration-based approach, we make the following observations:

  1. Notice that at the end of the game (for time step \(T\)), the optimal value is obvious,

     \[\forall s \in \mathcal{S}: \quad V\_{T}^{\ast}(s):=\max \_{a \in \mathcal{A}} R^{(T)}(s, a)
     \tag{1}\]
  2. For another time step \(0 \leq t<T\), if we suppose that we know the optimal value function for the next time step \(V\_{t+1}^{\ast}\), then we have,

     \[\forall t<T, s \in \mathcal{S}: V\_{t}^{\ast}(s):=\max \_{a \in \mathcal{A}}\left[R^{(t)}(s, a)+\mathbb{E}\_{s^{\prime} \sim p\_{s a}^{(t)}}\left[V\_{t+1}^{\ast}\left(s^{\prime}\right)\right]\right]
     \tag{2}\]
* With these observations in mind, we can come up with a clever algorithm to solve for the optimal value function:

  1. Compute \(V\_{T}^{\ast}\) using equation \((1)\).
  2. For \(t=T-1, \ldots, 0\):
     + Compute \(V\_{t}^{\ast}\) using \(V\_{t+1}^{\ast}\) using equation \((2)\).
* Side note: We can interpret standard value iteration as a special case of this general case, but without keeping track of time. It turns out that in the standard setting, if we run value iteration for \(\mathrm{T}\) steps, we get a \(\gamma^{T}\) approximation of the optimal value iteration (geometric convergence).

### Theorem

* Let \(B\) denote the Bellman update and \(|f(x)|*{\infty}:=\sup \_{x}|f(x)|\). If \(V*{t}\) denotes the value function at the \(t^{th}\) step, then,

\[\begin{aligned}
\left\|V\_{t+1}-V^{\ast}\right\|\_{\infty} &=\left\|B\left(V\_{t}\right)-V^{\ast}\right\|\_{\infty} \\
& \leq \gamma\left\|V\_{t}-V^{\ast}\right\|\_{\infty} \\
& \leq \gamma^{t}\left\|V\_{1}-V^{\ast}\right\|\_{\infty}
\end{aligned}\]

* In other words, the Bellman operator \(B\) is a \(\gamma\)-contracting operator.

## Linear Quadratic Regulation (LQR)

* In this section, we’ll cover a special case of the finite-horizon setting described in Section 1, for which the exact solution is (easily) tractable. This model is widely used in robotics, and a common technique in many problems is to reduce the formulation to this framework.
* First, let’s describe the model’s assumptions. We place ourselves in the continuous setting, with,

\[\mathcal{S}=\mathbb{R}^{n}, \quad \mathcal{A}=\mathbb{R}^{d}\]

* and we’ll assume linear transitions (with noise),

  \[s\_{t+1}=A\_{t} s\_{t}+B\_{t} a\_{t}+w\_{t}\]
  + where \(A\_{t} \in R^{n \times n}, B\_{t} \in R^{n \times d}\) are matrices and \(w\_{t} \sim \mathcal{N}\left(0, \Sigma\_{t}\right)\) is some gaussian noise (with zero mean).
* As we’ll show soon, it turns out that the noise, as long as it has zero mean, does not impact the optimal policy!
* We’ll also assume quadratic rewards,

  \[R^{(t)}\left(s\_{t}, a\_{t}\right)=-s\_{t}^{\top} U\_{t} s\_{t}-a\_{t}^{\top} W\_{t} a\_{t}\]
  + where \(U\_{t} \in R^{n \times n}, W\_{t} \in R^{d \times d}\) are positive definite matrices (meaning that the reward is always negative).
* **Remark:** Note that the quadratic formulation of the reward is equivalent to saying that we want our state to be close to the origin (where the reward is higher \()\). For example, if \(U\_{t}=I\_{n}\) (the identity matrix) and \(W\_{t}=I\_{d}\), then \(R\_{t}=-\left|s\_{t}\right|^2-\left|a\_{t}\right|^2\), meaning that we want to take smooth actions (small norm of \(a\_{t}\) to go back to the origin (small norm of \(s\_{t}\)). This could model a car trying to stay in the middle of lane without making impulsive moves!
* Now that we have defined the assumptions of our LQR model, let’s cover the 2 steps of the LQR algorithm.
* **Step 1:** suppose that we don’t know the matrices \(A, B, \Sigma\). To estimate them, we can follow the ideas outlined in the Value Approximation section of the RL notes. First, collect transitions from an arbitrary policy. Then, use linear regression to find:

\[\operatorname\*{arg\,min}\_{A, B} \sum\_{i=1}^{m} \sum\_{t=0}^{T-1}\left\|s\_{t+1}^{(i)}-\left(A s\_{t}^{(i)}+B a\_{t}^{(i)}\right)\right\|^2\]

* Finally, use a technique seen in Gaussian Discriminant Analysis to learn \(\Sigma\).
* **Step 2:** assuming that the parameters of our model are known (given or estimated with step 1), we can derive the optimal policy using dynamic programming.
* In other words, given

\[\left\{\begin{array}{ll}
s\_{t+1} & =A\_{t} s\_{t}+B\_{t} a\_{t}+w\_{t} \quad A\_{t}, B\_{t}, U\_{t}, W\_{t}, \Sigma\_{t} \text { known } \\
R^{(t)}\left(s\_{t}, a\_{t}\right) & =-s\_{t}^{\top} U\_{t} s\_{t}-a\_{t}^{\top} W\_{t} a\_{t}
\end{array}\right.\]

* we want to compute \(V\_{t}^{\ast}\). If we go back to section 1, we can apply dynamic programming, which yields,

  1. **Initialization step:**

     + For the last time step \(T\),\[\begin{aligned}
     V\_{T}^{\ast}\left(s\_{T}\right) &=\max \_{a\_{T} \in \mathcal{A}} R\_{T}\left(s\_{T}, a\_{T}\right) \\
     &=\max \_{a\_{T} \in \mathcal{A}}-s\_{T}^{\top} U\_{T} s\_{T}-a\_{T}^{\top} W\_{t} a\_{T} \\
     &=-s\_{T}^{\top} U\_{t} s\_{T} \quad \text { (maximized for } \left.a\_{T}=0\right)
     \end{aligned}\]
  2. **Recurrence step:**

     + Let \(t<T\). Suppose we know \(V\_{t+1}^{\ast}\).
     + **Fact 1:** It can be shown that if \(V\_{t+1}^{\ast}\) is a quadratic function in \(s\_{t}\), then \(V\_{t}^{\ast}\) is also a quadratic function. In other words, there exists some matrix \(\Phi\) and some scalar \(\Psi\) such that,\[\begin{array}{l}
     \text { if } V\_{t+1}^{\ast}\left(s\_{t+1}\right)=s\_{t+1}^{\top} \Phi\_{t+1} s\_{t+1}+\Psi\_{t+1} \\
     \text { then } V\_{t}^{\ast}\left(s\_{t}\right)=s\_{t}^{\top} \Phi\_{t} s\_{t}+\Psi\_{t}
     \end{array}\]
     + For time step \(t=T\), we had \(\Phi\_{t}=-U\_{T}\) and \(\Psi\_{T}=0\).
     + **Fact 2:** We can show that the optimal policy is just a linear function of the state.
     + Knowing \(V\_{t+1}^{\ast}\) is equivalent to knowing \(\Phi\_{t+1}\) and \(\Psi\_{t+1}\), so we just need to explain how we compute \(\Phi\_{t}\) and \(\Psi\_{t}\) from \(\Phi\_{t+1}\) and \(\Psi\_{t+1}\) and the other parameters of the problem.

       \[\begin{aligned}
       V\_{t}^{\ast}\left(s\_{t}\right) &=s\_{t}^{\top} \Phi\_{t} s\_{t}+\Psi\_{t} \\
       &=\max \_{a t}\left[R^{(t)}\left(s\_{t}, a\_{t}\right)+\mathbb{E}\_{s\_{t+1} \sim p\_{s t}^{(t)} a\_{t}}\left[V\_{t+1}^{\ast}\left(s\_{t+1}\right)\right]\right] \\
       &=\max \_{a\_{t}}\left[-s\_{t}^{\top} U\_{t} s\_{t}-a\_{t}^{\top} V\_{t} a\_{t}+\mathbb{E}\_{s\_{t+1} \sim \mathcal{N}\left(A\_{t} s\_{t}+B\_{t} a\_{t}, \Sigma\_{t}\right)}\left[s\_{t+1}^{\top} \Phi\_{t+1} s\_{t+1}+\Psi\_{t+1}\right]\right]
       \end{aligned}\]
       - where the second line is just the definition of the optimal value function and the third line is obtained by plugging in the dynamics of our model along with the quadratic assumption. Notice that the last expression is a quadratic function in \(a\_{t}\) and can thus be (easily) optimized, using the identity \(\mathbb{E}\left[w\_{t}^{\top} \Phi\_{t+1} w\_{t}\right]=\operatorname{Tr}\left(\Sigma\_{t} \Phi\_{t+1}\right)\) with \(w\_{t} \sim \mathcal{N}\left(0, \Sigma\_{t}\right)\).
     + We get the optimal action \(a\_{t}^{\ast}\).

       \[\begin{aligned}
       a\_{t}^{\ast} &=\left[\left(B\_{t}^{\top} \Phi\_{t+1} B\_{t}-V\_{t}\right)^{-1} B\_{t} \Phi\_{t+1} A\_{t}\right] \cdot s\_{t} \\
       &=L\_{t} \cdot s\_{t}
       \end{aligned}\]
       - where,\[L\_{t}:=\left[\left(B\_{t}^{\top} \Phi\_{t+1} B\_{t}-W\_{t}\right)^{-1} B\_{t} \Phi\_{t+1} A\_{t}\right]\]
     + which is an impressive result: our optimal policy is linear in \(s\_{t}\). Given \(a\_{t}^{\ast}\) we can solve for \(\Phi\_{t}\) and \(\Psi\_{t}\). We finally get the **Discrete Ricatti** equations,\[\begin{array}{l}
     \Phi\_{t}=A\_{t}^{\top}\left(\Phi\_{t+1}-\Phi\_{t+1} B\_{t}\left(B\_{t}^{\top} \Phi\_{t+1} B\_{t}-W\_{t}\right)^{-1} B\_{t} \Phi\_{t+1}\right) A\_{t}-U\_{t} \\
     \Psi\_{t}=-\operatorname{tr}\left(\Sigma\_{t} \Phi\_{t+1}\right)+\Psi\_{t+1}
     \end{array}\]
     + **Fact 3:** we notice that \(\Phi\_{t}\) depends on neither \(\Psi\) nor the noise \(\Sigma\_{t}!\) As \(L\_{t}\) is a function of \(A\_{t}, B\_{t}\) and \(\Phi\_{t+1}\), it implies that the optimal policy also does not depend on the noise! (But \(\Psi\_{t}\) does depend on \(\Sigma\_{t}\), which implies that \(V\_{t}^{\ast}\) depends on \(\Sigma\_{t}\).)
     + Using Fact 3, we can be even more clever and make our algorithm run (slightly) faster! As the optimal policy does not depend on \(\Psi\_{t}\), and the update of \(\Phi\_{t}\) only depends on \(\Phi\_{t}\), it is sufficient to update only \(\Phi\_{t}!\).
* **Key takeways**

  + To summarize, the LQR algorithm works as follows:
    1. (if necessary) estimate parameters \(A\_{t}, B\_{t}, \Sigma\_{t}\).
    2. initialize \(\Phi\_{T}:=-U\_{T}\) and \(\Psi\_{T}:=0\).
    3. iterate from \(t=T-1 \ldots 0\) to update \(\Phi\_{t}\) and \(\Psi\_{t}\) using \(\Phi\_{t+1}\) and \(\Psi\_{t+1}\) using the discrete Ricatti equations. If there exists a policy that drives the state towards zero, then convergence is guaranteed!

## From non-linear dynamics to LQR

* It turns out that a lot of problems can be reduced to LQR, even if dynamics are non-linear. While \(\mathrm{LQR}\) is a nice formulation because we are able to come up with a nice exact solution, it is far from being general. Let’s take for instance the case of the inverted pendulum. The transitions between states look like

  \[\left(\begin{array}{c}
  x\_{t+1} \\
  \dot{x}\_{t+1} \\
  \theta\_{t+1} \\
  \dot{\theta}\_{t+1}
  \end{array}\right)=F\left(\left(\begin{array}{c}
  x\_{t} \\
  \dot{x}\_{t} \\
  \theta\_{t} \\
  \dot{\theta}\_{t}
  \end{array}\right), a\_{t}\right)\]
  + where the function \(F\) depends on the cos of the angle etc. Now, the question we may ask is: “Can we linearize this system?”

### Linearization of dynamics

* Let’s suppose that at time \(t\), the system spends most of its time in some state \(\bar{s}\_t\) and the actions we perform are around \(\bar{a}\_t\). For the inverted pendulum, if we reached some kind of optimal, this is true: our actions are small and we don’t deviate much from the vertical.
* We are going to use Taylor expansion to linearize the dynamics. In the simple case where the state is one-dimensional and the transition function \(F\) does not depend on the action, we would write something like,

\[s\_{t+1}=F\left(s\_{t}\right) \approx F\left(\bar{s}\_{t}\right)+F^{\prime}\left(\bar{s}\_{t}\right) \cdot\left(s\_{t}-\bar{s}\_{t}\right)\]

* In the more general setting, the formula looks the same, with gradients instead of simple derivatives,

\[s\_{t+1} \approx F\left(\bar{s}\_{t}, \bar{a}\_{t}\right)+\nabla\_{s} F\left(\bar{s}\_{t}, \bar{a}\_{t}\right) \cdot\left(s\_{t}-\bar{s}\_{t}\right)+\nabla\_{a} F\left(\bar{s}\_{t}, \bar{a}\_{t}\right) \cdot\left(a\_{t}-\bar{a}\_{t}\right)
\tag{3}\]

* and now, \(s\_{t+1}\) is linear in \(s\_{t}\) and \(a\_{t}\), because we can rewrite equation \((3)\) as,

  \[s\_{t+1} \approx A s\_{t}+B s\_{t}+\kappa\]
  + where \(\kappa\) is some constant and \(A, B\) are matrices. Now, this writing looks awfully similar to the assumptions made for LQR. We just have to get rid of the constant term \(\kappa!\) It turns out that the constant term can be absorbed into \(s\_{t}\) by artificially increasing the dimension by one. This is the same trick that we used at the beginning of the class for linear regression.

### Differential Dynamic Programming (DDP)

* The previous method works well for cases where the goal is to stay around some state \(s^{\ast}\) (think about the inverted pendulum, or a car having to stay in the middle of a lane). However, in some cases, the goal can be more complicated.
* We’ll cover a method that applies when our system has to follow some trajectory (think about a rocket). This method is going to discretize the trajectory into discrete time steps, and create intermediary goals around which we will be able to use the previous technique! This method is called Differential Dynamic Programming. The main steps are
* **Step 1:** come up with a nominal trajectory using a naive controller, that approximate the trajectory we want to follow. In other words, our controller is able to approximate the gold trajectory with,

\[s\_{0}^{\ast}, a\_{0}^{\ast} \rightarrow s\_{1}^{\ast}, a\_{1}^{\ast} \rightarrow \ldots\]

* **Step 2:** linearize the dynamics around each trajectory point \(s\_{t}^{\ast}\), in other words

  \[s\_{t+1} \approx F\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)+\nabla\_{s} F\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)\left(s\_{t}-s\_{t}^{\ast}\right)+\nabla\_{a} F\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)\left(a\_{t}-a\_{t}^{\ast}\right)\]
  + where \(s\_{t}, a\_{t}\) would be our current state and action.
* Now that we have a linear approximation around each of these points, we can use the previous section and rewrite,

\[s\_{t+1}=A\_{t} \cdot s\_{t}+B\_{t} \cdot a\_{t}\]

* Notice that in that case, we use the non-stationary dynamics setting that we mentioned in th section on .
* Note that we can apply a similar derivation for the reward \(R^{(t)}\), with a second-order Taylor expansion.

  \[\begin{aligned}
  R\left(s\_{t}, a\_{t}\right) & \approx R\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)+\nabla\_{s} R\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)\left(s\_{t}-s\_{t}^{\ast}\right)+\nabla\_{a} R\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)\left(a\_{t}-a\_{t}^{\ast}\right) \\
  &+\frac{1}{2}\left(s\_{t}-s\_{t}^{\ast}\right)^{\top} H\_{s s}\left(s\_{t}-s\_{t}^{\ast}\right)+\left(s\_{t}-s\_{t}^{\ast}\right)^{\top} H\_{s a}\left(a\_{t}-a\_{t}^{\ast}\right) \\
  &+\frac{1}{2}\left(a\_{t}-a\_{t}^{\ast}\right)^{\top} H\_{a a}\left(a\_{t}-a\_{t}^{\ast}\right)
  \end{aligned}\]
  + where \(H\_{x y}\) refers to the entry of the Hessian of \(R\) with respect to \(x\) and \(y\) evaluated in \(\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)\) (omitted for readability). This expression can be re-written as,\[R\_{t}\left(s\_{t}, a\_{t}\right)=-s\_{t}^{\top} U\_{t} s\_{t}-a\_{t}^{\top} W\_{t} a\_{t}\]
* for some matrices \(U\_{t}, W\_{t}\), with the same trick of adding an extra dimension of ones. This follows from,

\[\left(\begin{array}{ll}
1 & x
\end{array}\right) \cdot\left(\begin{array}{ll}
a & b \\
b & c
\end{array}\right) \cdot\left(\begin{array}{l}
1 \\
x
\end{array}\right)=a+2 b x+c x^2\]

* **Step 3:** Note that our problem is now strictly re-written in the LQR framework. Let’s just use LQR to find the optimal policy \(\pi\_{t}\). As a result, our new controller will (hopefully) be better!
* Note: Some problems might arise if the LQR trajectory deviates too much from the linearized approximation of the trajectory, but that can be fixed with reward-shaping.
* **Step 4:** Now that we get a new controller (our new policy \(\left.\pi\_{t}\right)\), we use it to produce a new trajectory,

\[s\_{0}^{\ast}, \pi\_{0}\left(s\_{0}^{\ast}\right) \rightarrow s\_{1}^{\ast}, \pi\_{1}\left(s\_{1}^{\ast}\right) \rightarrow \rightarrow s\_{T}^{\ast}\]

* Note that when we generate this new trajectory, we use the real \(F\) and not its linear approximation to compute transitions, meaning that,

\[s\_{t+1}^{\ast}=F\left(s\_{t}^{\ast}, a\_{t}^{\ast}\right)\]

* Then, go back to step 2 and repeat until some stopping criterion.

## Linear Quadratic Gaussian (LQG)

* Often, in the real word, we don’t get to observe the full state \(s\_{t}\). For example, an autonomous car could receive an image from a camera, which is merely an observation, and not the full state of the world. So far, we assumed that the state was available. As this might not hold true for most of the real-world problems, we need a new tool to model this situation: Partially Observable MDPs (POMDPs).
* A POMDP is an MDP with an extra observation layer. In other words, we introduce a new variable \(o\_{t}\), that follows some conditional distribution given the current state \(s\_{t}\)

\[o\_{t}\left|s\_{t} \sim O(o \mid s)\right.\]

* Formally, a finite-horizon POMDP is given by a tuple,

\[\left(\mathcal{S}, \mathcal{O}, \mathcal{A}, p\_{s a}, T, R\right)\]

* Within this framework, the general strategy is to maintain a belief state (distribution over states) based on the observation \(o\_{1}, \ldots, o\_{t}\). Then, a policy in a POMDP maps belief states to actions.
* In this section, we’ll present a extension of LQR to this new setting. Assume that we observe \(y\_{t} \in \mathbb{R}^{m}\) with \(m<n\) such that,

  \[\left\{\begin{array}{l}
  y\_{t}=C \cdot s\_{t}+v\_{t} \\
  s\_{t+1}=A \cdot s\_{t}+B \cdot a\_{t}+w\_{t}
  \end{array}\right.\]
  + where \(C \in R^{m \times n}\) is a compression matrix and \(v\_{t}\) is the sensor noise (also gaussian, like \(w\_{t}\).
* Note that the reward function \(R^{(t)}\) is left unchanged, as a function of the state (not the observation) and action. Also, as distributions are gaussian, the belief state is also going to be gaussian. In this new framework, let’s give an overview of the strategy we are going to adopt to find the optimal policy:
  + **Step 1:** First, compute the distribution on the possible states (the belief state), based on the observations we have. In other words, we want to compute the mean \(s\_{t \mid t}\) and the covariance \(\Sigma\_{t \mid t}\) of,

    \[s\_{t} \mid y\_{1}, \ldots, y\_{t} \sim \mathcal{N}\left(s\_{t \mid t}, \Sigma\_{t \mid t}\right)\]
  + to perform the computation efficiently over time, we’ll use the Kalman Filter algorithm (used on-board Apollo Lunar Module!).
  + **Step 2:** Now that we have the distribution, we’ll use the mean \(s\_{t \mid t}\) as the best approximation for \(s\_{t}\)
  + **Step 3:** Then set the action \(a\_{t}:=L\_{t} s\_{t \mid t}\) where \(L\_{t}\) comes from the regular LQR algorithm.
* Intuitively, to understand why this works, notice that \(s\_{t \mid t}\) is a noisy approximation of \(s\_{t}\) (equivalent to adding more noise to LQR) but we proved that \(\mathrm{LQR}\) is independent of the noise!
* Step 1 needs to be explicated. We’ll cover a simple case where there is no action dependence in our dynamics (but the general case follows the same idea). Suppose that

\[\left\{\begin{array}{l}
s\_{t+1}=A \cdot s\_{t}+w\_{t}, \quad w\_{t} \sim N\left(0, \Sigma\_{s}\right) \\
y\_{t}=C \cdot s\_{t}+v\_{t}, \quad v\_{t} \sim N\left(0, \Sigma\_{y}\right)
\end{array}\right.\]

* As noises are Gaussians, we can easily prove that the joint distribution is also Gaussian then, using the marginal formulas of gaussians (see our treatment on [Factor Analysis](../factor-analysis)), we would get,

\[s\_{t} \mid y\_{1}, \ldots, y\_{t} \sim \mathcal{N}\left(s\_{t \mid t}, \Sigma\_{t \mid t}\right)\]

* However, computing the marginal distribution parameters using these formulas would be computationally expensive! It would require manipulating matrices of shape \(t \times t\). Recall that inverting a matrix can be done in \(O\left(t^{3}\right)\), and it would then have to be repeated over the time steps, yielding a cost in

\[O\left(t^{4}\right) !\]

* The Kalman filter algorithm provides a much better way of computing the mean and variance, by updating them over time in constant time in \(t!\) The kalman filter is based on two basics steps. Assume that we know the distribution of \(s\_{t} \mid y\_{1}, \ldots, y\_{t}\):

  + **Predict step:** compute \(s\_{t+1} \mid y\_{1}, \ldots, y\_{t}\)
  + **Update step:** compute \(s\_{t+1} \mid y\_{1}, \ldots, y\_{t+1}\)
* and iterate over time steps! The combination of the predict and update steps updates our belief states. In other words, the process looks like,

\[\left(s\_{t} \mid y\_{1}, \ldots, y\_{t}\right) \stackrel{\text { predict }}{\longrightarrow}\left(s\_{t+1} \mid y\_{1}, \ldots, y\_{t}\right) \stackrel{\text { update }}{\longrightarrow}\left(s\_{t+1} \mid y\_{1}, \ldots, y\_{t+1}\right) \stackrel{\text { predict }}{\longrightarrow} \ldots\]

* **Predict step:** Suppose that we know the distribution of,

\[s\_{t} \mid y\_{1}, \ldots, y\_{t} \sim \mathcal{N}\left(s\_{t \mid t}, \Sigma\_{t \mid t}\right)\]

* then, the distribution over the next state is also a gaussian distribution,

  \[s\_{t+1} \mid y\_{1}, \ldots, y\_{t} \sim \mathcal{N}\left(s\_{t+1 \mid t}, \Sigma\_{t+1 \mid t}\right)\]
  + where,\[\left\{\begin{array}{l}
  s\_{t+1 \mid t}=A \cdot s\_{t \mid t} \\
  \Sigma\_{t+1 \mid t}=A \cdot \Sigma\_{t \mid t} \cdot A^{\top}+\Sigma\_{s}
  \end{array}\right.\]
* **Update step:** given \(s\_{t+1 \mid t}\) and \(\Sigma\_{t+1 \mid t}\) such that,

\[s\_{t+1} \mid y\_{1}, \ldots, y\_{t} \sim \mathcal{N}\left(s\_{t+1 \mid t}, \Sigma\_{t+1 \mid t}\right)\]

* we can prove that,

  \[s\_{t+1} \mid y\_{1}, \ldots, y\_{t+1} \sim \mathcal{N}\left(s\_{t+1 \mid t+1}, \Sigma\_{t+1 \mid t+1}\right)\]
  + where,\[\left\{\begin{array}{ll}
  s\_{t+1 \mid t+1} & =s\_{t+1 \mid t}+K\_{t}\left(y\_{t+1}-C s\_{t+1 \mid t}\right) \\
  \Sigma\_{t+1 \mid t+1} & =\Sigma\_{t+1 \mid t}-K\_{t} \cdot C \cdot \Sigma\_{t+1 \mid t}
  \end{array}\right.\]
* with,

\[K\_{t}:=\Sigma\_{t+1 \mid t} C^{\top}\left(C \Sigma\_{t+1 \mid t} C^{\top}+\Sigma\_{y}\right)^{-1}\]

* The matrix \(K\_{t}\) is called the **Kalman gain**.
* Now, if we have a closer look at the formulas, we notice that we don’t need the observations prior to time step \(t!\) The update steps only depends on the previous distribution. Putting it all together, the algorithm first runs a forward pass to compute the \(K\_{t}, \Sigma\_{t \mid t}\) and \(s\_{t \mid t}\) (sometimes referred to as \(\hat{s}\) in literature). Then, it runs a backward pass (the LQR updates) to compute the quantities \(\Psi\_{t}, \Psi\_{t}\) and \(L\_{t}\). Finally, we recover the optimal policy with \(a\_{t}^{\ast}=L\_{t} s\_{t \mid t}\).

## References

* [CS229 Notes](http://cs229.stanford.edu/syllabus-summer2020.html).

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledLQRandDDPandLQG,
  title   = {Linear Quadratic Regulation, Differential Dynamic Programming and Linear Quadratic Gaussian},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS229: Machine Learning},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
