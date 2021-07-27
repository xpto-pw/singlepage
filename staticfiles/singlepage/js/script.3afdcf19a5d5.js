let corFundo=true;

function mudarFundo() {if(corFundo) {
        document.documentElement.style.setProperty('--fundo','blue');
    } else {
        document.documentElement.style.setProperty('--fundo','black');
    }
    corFundo = !corFundo;
}

let corLetra=true;

function mudarCorLetra() {
    if(corLetra) {
        document.documentElement.style.setProperty('--letraC','rgb(0, 255, 13)');
    } else {
        document.documentElement.style.setProperty('--letraC','red');
    }
    corLetra = !corLetra;
}

let fontLetra=true;

function mudarLetra() {
    if(fontLetra) {
        document.documentElement.style.setProperty('--letraF','italic');
    } else {
        document.documentElement.style.setProperty('--letraF','normal');
    }
    fontLetra = !fontLetra;
}


function showSection(section) {
    if (section==1){
        document.querySelector('#content2').style.display = 'none';

                 fetch(`/sections/${section}`)
                .then(response => response.json())
                .then(text => {
                    document.querySelector('#content').innerHTML = criarJogadores(text.jogadores).join("");
                    document.querySelector('#content').style.display = 'block';
                });
    }
    if (section==2){
        document.querySelector('#content').style.display = 'none';
        document.querySelector('#content2').style.display = 'block';
    }
}

            document.addEventListener('DOMContentLoaded', function() {
                document.querySelectorAll('button').forEach(button => {
                    button.onclick = function() {
                        showSection(this.dataset.section);
                    };
                });
            });


function criarJogadores(jogadores){
    jogadoresHTML = [];

    jogadores.map((j) => { jogadoresHTML.push(templateJogador(j)) });

    return jogadoresHTML;
}


function templateJogador(jogador){
    return template =
        `
         <section>
         <text>${jogador.nome}, ${jogador.apelido} -></text>
         <button onclick="paginaJogador('${jogador.nome}','${jogador.autor}','${jogador.apelido}','${jogador.clube}','${jogador.bio}')">${jogador.nome}</button>
         </section>
         <br>
        `;
}


function paginaJogador(nome, autor, apelido, clube, bio) {

    document.querySelector('#content').innerHTML =
        `
            <section>
            <h2>${nome}</h2>
            <h3>Autor da inserção: ${autor}</h3>
            <p>Nome: ${nome} </p>
            <br>
            <p>Apelido: ${apelido} </p>
            <br>
            <p>Clube Atual: ${clube} </p>
            <br>
            <p>Bio: ${bio} </p>
            </section>
            `;
}

