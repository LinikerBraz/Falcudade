public class Principal{
    public static void main(String[] args){
        Aluno aluno1 = new Aluno("Luiz Liniker", "Waldir Lisboa, 258","(35) 99755-3071", "linikerbraz32@gmail.com", "A0035");
        Aluno aluno2 = new Aluno("Vanessa Maia", "Santa Cruz, 582","(35) 998754-7159", "maia.vanessa32@gmail.com", "A0014");

        System.out.println("Informações do Aluno 1:");
        System.out.println(aluno1);
        System.out.println("\nInformações do Aluno 2:");
        System.out.println(aluno2);
    }
}