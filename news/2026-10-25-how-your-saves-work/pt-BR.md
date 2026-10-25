O seu progresso é a coisa mais importante que você traz para o Infinity, então aqui vai exatamente como o launcher cuida dos seus saves.

## Os saves ficam onde o jogo coloca

O Infinity não guarda cópia dos seus saves em nenhum outro lugar. Eles ficam na própria pasta de saves do Azimuth:

`<Azimuth>\data\titles\1A96545B\saves\player-1\`

## Uma pasta por perfil

Cada perfil do Infinity tem a sua própria identidade e, portanto, a sua própria pasta de save (`User_…`), lado a lado em `player-1`. Perfis nunca compartilham um save.

- **Perfis offline** que você cria sem entrar também ganham cada um a sua pasta.
- **Ao enviar um perfil Noob** para a sua conta quando você entra, o último save offline dele é copiado para a identidade online, e você continua a mesma carreira offline e online.
- **O Hardcore** funciona diferente: a carreira online começa do zero pelo servidor, e o progresso Hardcore offline nunca é enviado.

## Revisões: o jogo guarda as duas mais novas

Cada vez que o jogo salva, ele grava uma nova *revisão*. Uma revisão só vale quando está completa: todos os arquivos batem com a lista que o jogo gravou junto. O jogo sempre carrega a revisão completa mais nova e guarda as duas mais recentes.

## Comece por um save que você já tem

Ao criar um perfil, você pode começar a partir de qualquer save que já esteja no seu PC — eles aparecem do mais recente para o mais antigo, com nível e créditos. O seu save original é só lido, nunca alterado. O launcher faz uma cópia, confere cada arquivo e só então transforma essa cópia na revisão mais nova do perfil. Isso só acontece com o jogo fechado, e se algo der errado no meio do caminho, o perfil fica exatamente como estava.

## Nada é apagado

Sempre que o launcher precisa tirar algo do caminho — uma revisão incompleta, um save mais antigo que ele substitui, uma versão da nuvem, um conflito — ele primeiro copia para:

`saves\fi-launcher-archive\<User_…>\`

## Saves na nuvem

Só os perfis **Infinity Supporter** no modo **Hardcore** têm save na nuvem. Todos os outros perfis ficam apenas no seu PC.

Para esses perfis, a cada sessão de jogo:

- **Antes de o jogo abrir,** o launcher reenvia o que não subiu da última vez, separa revisões incompletas e instala uma revisão mais nova da nuvem, se houver.
- **Se algo parecer errado,** como um conflito ou um save ainda sendo gravado, o jogo não abre em vez de arriscar.
- **Depois que você sai,** a sua revisão completa mais nova é enviada. Se o envio falhar, ele fica pendente e é tentado de novo na próxima vez que você abrir o jogo.

## Pinturas são por PC

As suas criações (pinturas e as miniaturas delas) são compartilhadas por todos os perfis do mesmo PC e não vão para a nuvem.

## Bons hábitos

- Feche o jogo antes de mexer na pasta de saves.
- De vez em quando, faça o seu próprio backup de `player-1` — não custa nada.
