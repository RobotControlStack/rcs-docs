# Usage
The python package is called `rcs`.
Import the library in python:
```python
import rcs
```
Checkout the python examples that we provide in [python/examples](python/examples):
- [fr3.py](python/examples/fr3.py) shows direct robot control with RCS's python bindings
- [env_joint_control.py](python/examples/env_joint_control.py) and [env_cartesian_control.py](python/examples/env_cartesian_control.py) demonstrates RCS's high level [gymnasium](https://gymnasium.farama.org/) interface both for joint- and end effector space control
All of these examples work both in the MuJoCo simulation as well as on your hardware FR3.
Just switch between the following settings in the example script
```python
ROBOT_INSTANCE = RobotPlatform.SIMULATION
# ROBOT_INSTANCE = RobotPlatform.HARDWARE
```
and add your robot credentials to a `.env` file like this:
```env
DESK_USERNAME=...
DESK_PASSWORD=...
```

## Command Line Interface
The package includes a command line interface which define useful commands to handle the FR3 robot without the need to use the Desk Website.
To list all available subcommands use:
```shell
python -m rcs --help
```