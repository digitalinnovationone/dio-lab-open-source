```python
class Musician:

    def __init__(self, name: str, age: int, college: str, languages: list[str],
                programming: dict[str, list[str]], instruments: list[str]):
        self.name        = name
        self.age         = age
        self.college     = college
        self.languages   = languages
        self.programming = programming
        self.instruments = instruments

def main():
    littleMe = Musician(
        name        = 'Guilherme Xavier Zanetti "zanettIno"',
        age         = 19,
        college     = "Fatec SCS",
        languages   = ["Português", "English"],
        programming = { "technologies": ["Python", "JavaScript", "Typescript", "Kotlin", "C"],
                        "frameworks":   ["Flask", "Node.js", "React", "Express", "Ktor"]},
        instruments = ["Drums", "General Percussion", "Violin"])

main()
```
<br>
<div align="center">
  <img height="160em" src="https://github-readme-stats.vercel.app/api?username=zanettIno&show_icons=true&theme=radical&count_private=true"/> &nbsp;
  <img height="160em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=zanettIno&layout=compact&theme=radical"/>
</div>
