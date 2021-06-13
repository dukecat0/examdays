# Examdays

*A Python module that helps you to calculate how many days will you have for preparing your exam.*

Module used:
[Pendulum](https://pypi.org/project/pendulum/)

## Usage

```python
from examdays import exam

exam(end_year, end_month, end_day)

# For example
# exam(2021, 6, 28)

```
or in Command Line:

```shell
$ examdays [end year] [end month] [end day] 
```

If you want to use specific colour in the output:

```shell
$ examdays [end year] [end month] [end day] [colour]
```

### Colour List:

+ BLACK
+ RED 
+ GREEN 
+ YELLOW 
+ BLUE 
+ MAGENTA
+ CYAN
+ WHITE 


## Example

```shell
$ examdays 2021 6 20
```

Output:
```shell
You still have: 6 days!
Good Luck! 
```

```shell
$ examdays 2021 6 30 YELLOW
```
Output:

[Yellow](./yellow.png)

```shell
$ examdays 2021 6 30 blue
```

Output:

[Blue](./blue.png)

