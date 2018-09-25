# Help ECE241
## TruthTable
Generate simple TruthTable from Logic expression
- Example:
```python
from logic.logicElements import LogicSignal
...
print_table(exps_to_table(lambda a,b,s: a * ~s + b * s))
```
