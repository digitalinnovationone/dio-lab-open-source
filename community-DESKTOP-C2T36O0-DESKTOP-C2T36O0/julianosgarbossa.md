# Juliano Sgarbossa

```swift
struct Developer {
    let name = "Juliano Sgarbossa"
    let role = "iOS Developer"
    let location = "Brazil - RS"
    let skills = [
        "Swift", 
        "UIKit (View Code)", 
        "SwiftUI", 
        "MVVM", 
        "Firebase"
    ]
    let learning = ["Core Data", "Keychain", "Vapor"]
    let hobbies = ["Coding 💻", "Reading 📚", "Soccer ⚽️"]
    
    func introduceYourself() {
        print("""
        Olá! 👋
        
        Eu sou o \(name), um \(role) que mora no \(location).
        
        Algumas das minhas habilidades são:
        \(skills.joined(separator: ", ")).
        
        Estou sempre buscando aprender coisas novas, como:
        \(learning.joined(separator: ", ")).
        
        E nos meus momentos livres, gosto de:
        \(hobbies.joined(separator: ", ")).

        Seja bem vindo ao meu perfil e é um prazer conhecer você!
        --------------------------------------------------------
        """)
    }
}

let me = Developer()
me.introduceYourself()
```

### Conecte-se comigo

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://www.dio.me/users/contato_julianosgarbossa)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://github.com/julianosgarbossa)


