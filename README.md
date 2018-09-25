# Help ECE241
## TruthTable (Python)
1. '~' represents NOT
2. '+' / '|' represents OR
3. '*' / '&' represents AND
Generate simple TruthTable from Logic expression
- Example:
```python
from logic.logicElements import LogicSignal
...
print_table(exps_to_table(lambda a,b,s: a * ~s + b * s))
```
