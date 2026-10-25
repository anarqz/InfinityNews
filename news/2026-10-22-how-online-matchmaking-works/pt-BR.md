Uma pequena explicação sobre o matchmaking online, porque vejo muitos de vocês confusos ou até bravos por não conseguirem jogar online.

## As partidas rodam nos computadores dos jogadores

O matchmaking ajuda os jogadores a se encontrarem, mas não repassa o tráfego do jogo. Numa partida, o **anfitrião** é o relay: ele recebe os pacotes de todos os jogadores e os compartilha com todo mundo, para que o lobby inteiro fique sincronizado.

O que o Infinity oferece é uma camada de matchmaking. Ela poupa todo mundo do trabalho de saber o seu IP para entrar na sua partida.

Isso não significa que o Infinity garanta uma experiência online estável ou corridas com baixa latência. No fim, você continua se conectando aos servidores locais de outras pessoas, e dependendo da conexão delas e das restrições do provedor.

## Hospedar exige uma porta aberta

- O seu roteador precisa redirecionar a **porta UDP 5101** para o seu computador.
- O seu firewall e o seu provedor precisam permitir conexões de entrada.
- Restrições do provedor como **CGNAT** podem impedir a hospedagem mesmo com o redirecionamento de porta configurado.

Entrar e hospedar têm requisitos de rede diferentes, e os dois precisam estar livres de restrições para a experiência online funcionar bem.

## Caiu logo depois de entrar?

Se às vezes você entra num lobby e é desconectado na hora, é o seu provedor ou o seu roteador, não o Infinity.

## Resumindo

Sem um relay oficial dedicado carregando o tráfego, algumas combinações de jogadores e redes simplesmente não conseguem se conectar. É assim desde o começo dos tempos.
