# Análise Funcionáros Vendas

![GitHub repo size](https://img.shields.io/github/repo-size/cemeterydriiver/analiseFuncionariosVendas?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/cemeterydriiver/analiseFuncionariosVendas?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/cemeterydriiver/analiseFuncionariosVendas?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/cemeterydriiver/analiseFuncionariosVendas?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/cemeterydriiver/analiseFuncionariosVendas?style=for-the-badge)


> Este é um código em Python que utiliza as bibliotecas Pandas, Openpyxl e Twilio para processar dados de vendas mensais e enviar mensagens SMS quando um vendedor atinge uma meta de vendas específica.

## 💻 Pré-requisitos
Antes de executar o código, certifique-se de ter as seguintes bibliotecas instaladas:

- [Pandas](https://pandas.pydata.org/)
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [Twilio](https://pages.twilio.com/twilio-brand-sales-pt-1?utm_source=google&utm_medium=cpc&utm_term=twilio&utm_campaign=G_S_LATAM_Brand_Twilio_Portuguese&cq_plac=&cq_net=g&cq_pos=&cq_med=&cq_plt=gp&gad=1&gclid=Cj0KCQjw1_SkBhDwARIsANbGpFvOU2svjs_0LEgtkjYgqLrNcqtQYp7oprnZ3k7v0DNlNTktMZSw5t4aAtBgEALw_wcB)

**Para instalar as bibliotecas necessárias, execute o seguinte comando:**
```bash
  pip install pandas openpyxl twilio
```
## ⚙️ Funcionalidades
O código realiza as seguintes funcionalidades:

- Lê arquivos Excel contendo dados de vendas mensais.
- Verifica se algum vendedor atingiu a meta de vendas de R$55.000,00.
- Envia uma mensagem SMS para um número específico informando o vendedor e a quantidade de vendas.

## 🦾 Como funciona
> O código utiliza a biblioteca Pandas para ler os arquivos Excel correspondentes aos meses de janeiro a junho. Em seguida, verifica se algum vendedor atingiu a meta de vendas de R$55.000,00. Se a meta for alcançada, é enviada uma mensagem SMS utilizando a biblioteca Twilio, informando o vendedor e a quantidade de vendas.

## 🏃 Executando a aplicação
**Para executar a aplicação, siga os passos abaixo:**

1. Certifique-se de ter as bibliotecas Pandas, Openpyxl e Twilio instaladas (consulte a seção de Pré-requisitos).
  
2. Clone o repositório
```bash
https://github.com/cemeterydriiver/analiseFuncionariosVendas.git
```
3. Abra o repositório na IDE de sua preferência, recomendo o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/)
  
4. Substitua as variáveis `account_sid` e `auth_token` com suas credenciais fornecidas pela Twilio.
   
5. Substitua `"+numero"` pelo número de telefone de destino e `"+numeroTwilio"` pelo número de telefone Twilio no qual as mensagens serão enviadas.
   
6. Certifique-se de ter arquivos Excel nomeados como janeiro.xlsx, fevereiro.xlsx, etc., contendo os dados de vendas do respectivo mês.
   
7. Execute o código e aguarde a saída do console para verificar se algum vendedor atingiu a meta e se as mensagens SMS foram enviadas.

## 🤝 Autores


<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/102593108?v=4" width="100px;" alt="Foto do ash no GitHub"/><br>
        <sub>
          <b>Ashlyn Iero</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

[⬆ Voltar ao topo](#Análise-Funcionáros-Vendas)<br>
