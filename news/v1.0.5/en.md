Infinity Horizon 1.0.5

### Download
Download **infinity-horizon-1.0.5-windows-x64.zip**, extract the entire archive into its own folder outside the Azimuth installation, and run **infinity.exe**. Keep the bundled files and signature sidecars together. Use **Configure** to ensure the included hook 79 is installed before playing online.

### Changes
- Keep the hosted world's UDP port mapping alive while the world waits for players. Some routers drop idle UDP mappings in under 25 seconds and gave the world a new public port, so players joining were sent to a port that no longer existed.
- When the world's public port still changes, tell matchmaking right away instead of waiting for the next regular update.
- Connection diagnostics now record whether the host received a joining player's network hints, sent its connection probes, and whether any send failed.

The package includes the Windows x64 launcher, updater, hook 79, overlay, English/Portuguese translations and license notices. Hook 79 is unchanged from 1.0.4. Game and Azimuth files are not included.

Validation: 1,878 Windows non-live tests passed, including 4 new tests for these changes. Real multiplayer and Proton validation are still pending. Create fresh lobbies and test both hosting directions.

The JSON descriptor and detached signature support authenticated automatic updates.

**SHA-256 (ZIP):** `493cf8b63ed6edc54a6616def5372750475417c44fe58f88d292d589164cc85a`

### Português
Baixe o ZIP, extraia todo o conteúdo em uma pasta própria fora da instalação do Azimuth e execute **infinity.exe**. Use **Configure** para garantir que o hook 79 esteja instalado.

Esta versão mantém ativo o mapeamento da porta UDP do mundo hospedado enquanto ele espera jogadores. Alguns roteadores descartam mapeamentos UDP ociosos em menos de 25 segundos e trocavam a porta pública do mundo, fazendo quem entrava mirar uma porta que já não existia. Se a porta mudar mesmo assim, o matchmaking é avisado na hora. Os diagnósticos de conexão agora mostram se o anfitrião recebeu as dicas de rede de quem entra, se enviou as sondagens e se algum envio falhou.

Os 1.878 testes não-live no Windows passaram. A validação em partidas reais e no Proton continua pendente. Criem lobbies novos e testem os dois sentidos (cada um hospedando).

[Download and full notes](https://github.com/anarqz/InfinityHorizon/releases/tag/v1.0.5)
