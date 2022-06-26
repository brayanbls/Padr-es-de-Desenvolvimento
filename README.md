# Padroes-de-Desenvolvimento

A palavra Facade que significa Fachada em português resume bem o objetivo deste padrão. Basicamente este padrão de projeto simplifica o código em uma especie de inteface que contem variadas funcionalidades providas de outras classes. Esta fachada atua como facilitadora, pois ao invés de importar diversas classes em cada código é possível importar somente a interface que já contém tudo dentro dela.

Imagine que você tenha um código que precisa inserir, deletar e selecionar dados de um banco de dados. Em todas as classes do código que precisar acessar essas funcionalidades dentro de uma classe, precisará importa-las. Utilizando uma fachada com as classes que deletem, inserem e selecionam, você precisará somente importar a fachada para obter as funcionalidades. Esta é um exemplo básico de como utilizar o padrão Facade.

Porém o Facade tem seu lado contra também, pois sempre que for implantar a fachada no seu código, automaticamente importará todas as classes que estão dentro dela, mesmo que algumas dessas classes não façam parte da sua lógica atual
