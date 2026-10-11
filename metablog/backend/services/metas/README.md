# services/metas —— 分层 git 引擎

机制同 memory.talk v5 的 metas：

- 每层一条权威分支 `layer/<名>`（线性，只放这一层的文件）；`stack` 是合并视图，每次层提交后一个 merge 节点。HEAD → stack。
- 始祖提交只有 `metas.json`：`layers[]`，最底在前。
- **一个动作一个提交**，subject 以 `[层名]` 开头。
- **守卫**：路径按后缀该归哪层，和声明的层不符即拒；路径已在别的层的树里即拒。
- 全部 plumbing（hash-object / update-index / write-tree / commit-tree / update-ref），服务进程是唯一写者。

| 文件 | 是什么 |
|---|---|
| `repo.py` | 仓库：初始化始祖、按层提交、读 stack 树、历史 |
| `git.py` | git plumbing 的薄封装 |
| `manager.py` | `MetasService`：对外的写 / 读入口，按协议校验 |
| `layers/` | 内置层协议：`origin.yaml` / `post.yaml` / `insight.yaml` + 协议解释器 `protocol.py` |
