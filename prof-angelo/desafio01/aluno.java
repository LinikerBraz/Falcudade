public class Aluno(){
    private String nome;
    private String endereco;
    private String telefone;
    private String email;
    private String matricula;
}

public Aluno(String nome, String endereco, String telefone, String email, String matricula){
    this.nome = nome;
    this.endereco = endereco;
    this.telefone = telefone;
    this.email = email;
    this.matricula = matricula;
}

public String toString(){
    return "Nome: " +nome "\n" +
            "Endereço: " +endereco "\n"+
            "Telefone: " +telefone "\n"+
            "E-mail: " +email "\n"+
            "Matricula: " +matricula;
}