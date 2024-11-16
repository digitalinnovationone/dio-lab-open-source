//Poliformismo no Kotlin

open class Profissional {                  // Super Classe.
    open fun trabalhar() {                 // Objeto.
        println("O profissional executa alguma função")
    }
}

class Advogado : Profissional() {               // Sub Classe.
    override fun trabalhar() {                  // Sobrescrita do método trabalhar() herdado da Super Classe.
        println("O advogado executa processos.")
    }
}

class Programador : Profissional() {         // Sub Classe.
    override fun trabalhar() {               // Sobrescrita do método trabalhar() herdado da Super Classe.
        println("O programador desenvolve códigos.")
    }
}

fun main() {
    val profissional1: Profissional = Advogado()  
    val profissional2: Profissional = Programador()      

    profissional1.trabalhar() // Chama o método da classe Advogado
    profissional2.trabalhar() // Chama o método da classe Programador
}

