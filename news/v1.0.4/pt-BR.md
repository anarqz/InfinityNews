Infinity Horizon 1.0.4

### Download
Download **infinity-horizon-1.0.4-windows-x64.zip**, extract the entire archive into its own folder outside the Azimuth installation, and run **infinity.exe**. Keep the bundled files and signature sidecars together. Use **Configure** to ensure the included hook 79 is installed before playing online.

### Changes
- Use a dedicated IPv4 HTTPS connection for matchmaking, keeping its observed address family consistent with IPv4 UDP port discovery.
- Apply the same transport to lobby announcements, heartbeats, joins, seat renewals and network hints.
- Bound DNS lookups and connection retries while preserving the official HTTPS hostname and certificate validation.
- Keep sign-in and downloads on their existing transport. No system IPv6 setting change is required.

The package includes the Windows x64 launcher, updater, hook 79, overlay, English/Portuguese translations and license notices. Hook 79 is unchanged from 1.0.3. Game and Azimuth files are not included.

Validation: 1,875 Windows non-live tests passed, including 12 transport regressions. The new transport still needs Proton and real multiplayer validation. Create fresh lobbies when retesting.

The JSON descriptor and detached signature support authenticated automatic updates.

**SHA-256 (ZIP):** `7b67a57c9b07b87445aa3ac9d7c56b66c2b4f8b28a9ab3b32e543044968fb52e`

### Português
Baixe o ZIP, extraia todo o conteúdo em uma pasta própria fora da instalação do Azimuth e execute **infinity.exe**. Use **Configure** para garantir que o hook 79 esteja instalado.

Esta versão usa uma conexão HTTPS IPv4 dedicada ao matchmaking para manter a família do endereço compatível com a descoberta de portas UDP em IPv4. Inclui limites de DNS e tentativas de conexão, preservando a validação HTTPS. Login e downloads mantêm o transporte existente; não é necessário desativar IPv6 no computador.

Os 1.875 testes não-live no Windows passaram. A validação do novo transporte no Proton e em partidas reais continua pendente. Criem lobbies novos ao testar. Arquivos do jogo e do Azimuth não estão incluídos.

[Download e notas completas](https://github.com/anarqz/InfinityHorizon/releases/tag/v1.0.4)
