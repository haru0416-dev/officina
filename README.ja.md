# Officina

[English](README.md)

普通のアイデア出しは一般論と単語の組み合わせに落ちる。「エージェント版 Notion」「AI-powered メモリ」「Durable Objects の X 向け」がその典型。

Officina は、その代わりに Labs 型のプリミティブだけを残す Skill。プロダクト案を推す前に、座席、制約の反転、潰すカテゴリ、5 行 API、先行事例（既に打った primitive を含む）、OSS の楔、kill-probe を書かせる。書けないカードは公開で kill する。

ここでの Skill は、エージェントが読み込む小さなパッケージ。`SKILL.md` に加え、参照・例・評価・スクリプトを置ける。

Status: experimental. 保存してある比較は 1 本だけで、ベンチマークではない。generic-idea の fixture では Officina が 16/16、baseline が 0/16。測れたのは mashup の抑制と primitive の鋭さであり、残ったカードが当たる証明ではない。

```txt
Seat
-> Recurring Friction
-> Constraint Inversion
-> Category Collapse
-> Named Primitive
-> Inevitability Test
-> Genericness Kill-Gate
-> Prior-Art Scan
-> OSS Wedge
-> Kill-Probe
-> Labs Card
```

名前はラテン語 *officina*（工房）。アイデアを量産する場ではなく、primitive を打つ作業台。

## なぜあるか

LLM は「独創的なアイデア」を次の盆地に写すのが得意。

```txt
agents + memory + dashboard -> AI-powered memory copilot
edge + database -> Durable Objects っぽいもの
Notion + agents -> Notion for agent thoughts
```

ピッチのリストが欲しいならそれでよい。欲しいのが Workers / R2 / AI SDK / Fluid / Workflow の形、つまり名前と API を持つ制約の反転なら、高い。

Officina は後者向け。

## 何ではないか

- 事業戦略が新しいという主張ではない
- リサーチ・評価・実装の代替ではない
- 毎回使う万能プロンプトではない
- アイデアリストを長くする方法ではない
- 仮定を mutation して発想を広げる Skill ではない
- それ自体が市場価値の証明ではない

狭い主張はこれだけ。

```txt
Labs 型の primitive 抽出は、kill-gate と claimed リストと評価フック付きの
エージェント実行可能な Skill として梱包できる。
```

## 向くとき

最初のアイデアリストを受け入れるコストが大きいとき。

- Labs / 企業 OSS の楔として次に何を打つか
- CDN を持たない個人の座席での primitive 設計
- X-for-Y と AI-powered X の停止
- スパイク前の「これがあるべき」のレビュー

向かないとき: 直接実装、短い事実、書き換え、解が既に決まっている作業。既知の方針に対する「普通じゃない代替案」だけが欲しいとき（それは別の ideation）。

## インストール

Node.js 20 以降。

npm 公開後、Codex と Claude Code の両方へ:

```bash
npx officina-skill install --all
```

片方だけ:

```bash
npx officina-skill install --codex
npx officina-skill install --claude
```

状態確認:

```bash
npx officina-skill doctor
```

コピー先:

```txt
~/.codex/skills/officina
~/.claude/skills/officina
```

公開前は GitHub から:

```bash
npx --package github:OWNER/officina officina-skill install --all
```

`OWNER` をリポジトリのオーナーに置き換える。

クローン済みなら:

```bash
node bin/officina-skill.js install --all
```

そのあと、アイデア・Labs・「次に何を作るか」で `officina` を使うようエージェントに頼む。Skill 非対応のランタイムでは `SKILL.md` を手順プロンプトとして使い、参照は必要なときだけ読む。

## 実戦で何が変わるか

こうなりにくい:

```txt
AI-powered メモリ、durable agents、思考用 Notion、ダッシュボード。
```

こうなりやすい:

```txt
座席: coding-agent セッションの assembler。
反転: 制約を落とすことが安くではなく、違法になる。
崩壊: veto を守る手段としての session summary / memory SaaS。
API: staple.put / budget / compact (throws) / assemble。
Kill: rejected path の再開率が同じなら止める。
```

長くすることが目的ではない。primitive までの道をレビュー可能にし、mashup を kill 列に残すことが目的。

## 評価

```bash
npm run check
npm run pack:dry
```

詳細は英語 README と `evals/`。

## 一文

Officina はエージェント向けの primitive コンパイラ。アイデア要求を、名前付きで殺せる Labs カードの短いカタログに落とす。落とせなければ何も推さない。

## License

MIT. See [LICENSE](LICENSE).
