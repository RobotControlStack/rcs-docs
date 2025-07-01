# Usage
The python package is called `rcs`.

## Direct Robot Control
Simple direct robot control:
```python
import rcs
from rcs import sim
from rcs._core.sim import CameraType
from rcs.camera.sim import SimCameraConfig, SimCameraSet
simulation = sim.Sim(rcs.scenes["fr3_empty_world"]["mjb"])
urdf_path = rcs.scenes["fr3_empty_world"]["urdf"]
ik = rcs.common.RL(str(urdf_path))
cfg = sim.SimRobotConfig()
cfg.add_id("0")
cfg.tcp_offset = rcs.common.Pose(rcs.common.FrankaHandTCPOffset())
robot = rcs.sim.SimRobot(simulation, ik, cfg)

gripper_cfg_sim = sim.SimGripperConfig()
gripper_cfg_sim.add_id("0")
gripper = sim.SimGripper(simulation, gripper_cfg_sim)

# add camera to have a rendering gui
cameras = {
    "wrist": SimCameraConfig(
        identifier="wrist_0",
        type=CameraType.fixed,
        resolution_width=640,
        resolution_height=480,
        frame_rate=30,
    ),
}
camera_set = SimCameraSet(simulation, cameras)
simulation.open_gui()
robot.set_cartesian_position(
    robot.get_cartesian_position() * rcs.common.Pose(translation=np.array([0.05, 0, 0]))
)
gripper.grasp()
simulation.step_until_convergence()
```
## Gym Env Interface
```python
from rcs.envs.creators import SimEnvCreator
from rcs.envs.utils import (
    default_mujoco_cameraset_cfg,
    default_sim_gripper_cfg,
    default_sim_robot_cfg,
)
from rcs.envs.base import ControlMode, RelativeTo
env_rel = SimEnvCreator()(
    control_mode=ControlMode.JOINTS,
    collision_guard=False,
    robot_cfg=default_sim_robot_cfg(),
    gripper_cfg=default_sim_gripper_cfg(),
    cameras=default_mujoco_cameraset_cfg(),
    max_relative_movement=np.deg2rad(5),
    relative_to=RelativeTo.LAST_STEP,
)
env_rel.get_wrapper_attr("sim").open_gui()

for _ in range(10):
    obs, info = env_rel.reset()
    for _ in range(10):
        # sample random relative action and execute it
        act = env_rel.action_space.sample()
        print(act)
        obs, reward, terminated, truncated, info = env_rel.step(act)
        print(obs)
        if truncated or terminated:
            logger.info("Truncated or terminated!")
            return
```
## Examples
Checkout the python examples in the [examples](examples) folder:
- [fr3_direct_control.py](examples/fr3.py) shows direct robot control with RCS's python bindings
- [fr3_env_joint_control.py](examples/env_joint_control.py) and [fr3_env_cartesian_control.py](examples/env_cartesian_control.py) demonstrates RCS's high level [gymnasium](https://gymnasium.farama.org/) interface both for joint- and end effector space control
All of these examples work both in the MuJoCo simulation as well as on your hardware FR3.


## Hardware Extensions
To enable hardware usage in RCS, install the needed hardware extensions via pip. RCS itself comes with a couple of supported extensions e.g. control of the FR3 via the [`rcs_fr3`](extensions/rcs_fr3) extension. All native supported extension are located in [extensions](extensions).
To install extensions:
```shell
pip install -ve extensions/rcs_fr3
```
For more details real the readme file of the respective extension.

After the required hardware extensions are installed the examples also above work on real hardware:
Switch to hardware by setting the following flag:
```python
ROBOT_INSTANCE = RobotPlatform.SIMULATION
# ROBOT_INSTANCE = RobotPlatform.HARDWARE
```

### Command Line Interface
Some modules include command line interfaces, e.g. rcs_fr3 defines useful commands to handle the FR3 robot without the need to use the Desk Website.
You can see the available subcommands as follows:
```shell
python -m rcs_fr3 --help
python -m rcs_realsense --help
```