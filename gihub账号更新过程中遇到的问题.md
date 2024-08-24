~~~
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
~~~

这条消息表示 GitHub 自 2021 年 8 月 13 日起已经不再支持使用密码进行身份验证，这是为了增强账户的安全性。现在，GitHub 推荐使用更安全的身份验证方法，如使用 SSH 密钥或 GitHub 的个人访问令牌（Personal Access Tokens, PAT）结合 HTTPS URL 来进行 Git 操作。

以下是根据您的需求，如何配置和使用这些更安全的身份验证方法的步骤：

### 使用 SSH 密钥

1. 生成 SSH 密钥

   （如果您还没有的话）：

   - 在命令行中运行 `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`。按照提示操作，密钥将被保存在您的 `~/.ssh` 目录下。

2. 将 SSH 公钥添加到 GitHub

   - 在 GitHub 上，进入您的账户设置。
   - 点击“SSH and GPG keys”或类似的选项。
   - 点击“New SSH key”按钮，并将您的公钥（通常名为 `id_rsa.pub`）的内容粘贴到“Key”字段中。
   - 点击“Add SSH key”保存。

3. 配置 Git 使用 SSH URL

   ：

   - 查看您的 Git 仓库的 SSH URL（在 GitHub 仓库页面的“Code”选项卡下，点击“SSH”旁边的复制按钮）。
   - 使用 SSH URL 克隆或推送仓库。

### 使用个人访问令牌（PAT）

1. 生成个人访问令牌

   ：

   - 登录到 GitHub。
   - 进入“Settings”（设置）。
   - 点击“Developer settings”（开发者设置）。
   - 点击“Personal access tokens”（个人访问令牌）。
   - 点击“Generate new token”（生成新令牌）。
   - 选择所需的权限范围，然后点击“Generate token”（生成令牌）。
   - 复制生成的令牌，因为之后您将无法通过网页再次查看它。

2. 配置 Git 使用 HTTPS URL 和 PAT

   ：

   - 使用 HTTPS URL 克隆或推送仓库。
   - 在使用需要身份验证的命令（如 `git push`）时，Git 会提示您输入用户名和密码。在这里，您可以将用户名留空或输入您的 GitHub 用户名，并将密码替换为您的个人访问令牌。
   - 或者，您可以在 `~/.gitconfig` 文件中设置全局的 HTTPS 凭证助手（如 Git Credential Manager Core），以存储和管理您的令牌。

### 注意

- **保护您的个人访问令牌**：个人访问令牌具有与您的 GitHub 密码相同的访问权限，因此请务必妥善保管，不要将其硬编码在代码中或与他人共享。
- **定期更新您的令牌**：为了提高安全性，建议定期生成新的个人访问令牌，并撤销旧的令牌。
- **考虑使用双因素认证**：双因素认证为您的 GitHub 账户提供了额外的安全层，强烈建议启用。

在Windows 11家庭版中修改hosts文件，需要遵循一定的步骤来确保操作正确无误。以下是详细的步骤说明：

### 1. 找到hosts文件位置

hosts文件位于系统盘（通常是C盘）的特定目录下，具体路径为`C:\Windows\System32\drivers\etc\`。

### 2. 修改hosts文件权限

由于hosts文件位于系统文件夹中，默认情况下可能没有足够的权限进行修改。因此，需要先修改其文件权限。

- 右键点击hosts文件，选择“属性”。
- 在“属性”窗口中，取消勾选“只读”属性（如果已勾选）。
- 切换到“安全”选项卡，点击“编辑”按钮。
- 在弹出的权限窗口中，找到你的用户账户（或“管理员”账户），并勾选“允许”列下的“修改”和“读取&执行”、“读取”以及“写入”权限（确保这些权限被选中）。
- 点击“确定”保存更改。如果系统提示你确认更改，点击“是”。

### 3. 使用文本编辑器打开hosts文件

由于hosts文件是一个纯文本文件，你可以使用任何文本编辑器来打开它，但建议使用具有管理员权限的文本编辑器来避免权限问题。

- 按下`Win + S`组合键，打开搜索栏，输入“记事本”并选择“以管理员身份运行”。
- 在记事本中，点击左上角的“文件”菜单，选择“打开”。
- 在弹出的“打开”对话框中，导航到`C:\Windows\System32\drivers\etc\`目录，选择hosts文件，然后点击“打开”。

### 4. 修改hosts文件内容

在打开的hosts文件中，你可以根据需要添加或修改IP地址和主机名的映射关系。每个条目占据一行，格式为“IP地址 主机名”。

### 5. 保存并关闭hosts文件

在记事本中完成hosts文件的修改后，点击左上角的“文件”菜单，选择“保存”以保存更改，然后关闭记事本。

### 注意事项

- 在修改hosts文件时，请务必谨慎操作，因为不正确的条目可能会导致网络连接问题。
- 如果你不确定某个条目是否需要修改或添加，建议先进行备份，以便在出现问题时恢复原始设置。
- 修改hosts文件后，可能需要清除浏览器缓存或重启计算机才能使更改生效。

通过以上步骤，你可以在Windows 11家庭版中成功修改hosts文件。

要通过SSH连接到GitHub（或任何Git仓库），你需要先在你的计算机上设置SSH密钥，并将公钥添加到GitHub账户中。以下是一步步的指导：

### 1. 检查SSH密钥是否存在

首先，你需要检查你的计算机上是否已经有了SSH密钥。打开终端（在Windows上可以使用Git Bash或Windows Terminal），输入以下命令来检查SSH密钥：

```bash
bash复制代码

ls -al ~/.ssh
```

查看输出中是否有`id_rsa`和`id_rsa.pub`文件。`id_rsa`是你的私钥，`id_rsa.pub`是你的公钥。

- 如果这些文件存在，你可以选择使用它们（确保你记得这些密钥的密码，或者它们没有密码保护），或者生成新的密钥。
- 如果这些文件不存在，你需要生成新的密钥。

### 2. 生成新的SSH密钥（如果还没有的话）

如果你还没有SSH密钥，或者想要一个新的密钥，可以使用以下命令生成：

```bash
bash复制代码

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

将`your_email@example.com`替换为你的电子邮件地址。这个命令会提示你输入密钥的存储位置和密钥密码（可选）。如果你不想设置密码，只需在提示时按回车。

### 3. 将公钥添加到ssh-agent（可选）

如果你想要你的SSH密钥在每次登录时自动加载，可以将其添加到ssh-agent中。首先，启动ssh-agent（如果它还没有运行）：

```bash
bash复制代码

eval "$(ssh-agent -s)"
```

然后，将你的私钥添加到ssh-agent中：

```bash
bash复制代码

ssh-add ~/.ssh/id_rsa
```

### 4. 将公钥添加到GitHub

1. 打开你的`~/.ssh/id_rsa.pub`文件，复制里面的内容。
2. 登录到你的GitHub账户。
3. 点击右上角的头像，选择“Settings”（设置）。
4. 在侧边栏中，点击“SSH and GPG keys”（SSH和GPG密钥）。
5. 点击“New SSH key”（新建SSH密钥）。
6. 在“Title”（标题）字段中，给你的密钥起一个名字（例如，你的计算机名或邮箱）。
7. 在“Key”（密钥）字段中，粘贴你之前复制的公钥内容。
8. 点击“Add SSH key”（添加SSH密钥）。

### 5. 测试SSH连接

现在，你可以测试SSH连接是否成功。在终端中，输入以下命令：

```bash
bash复制代码

ssh -T git@github.com
```

如果一切设置正确，你会看到一条欢迎信息，表明你已经成功通过SSH连接到GitHub。

### 6. 使用SSH URL克隆仓库

现在，你可以使用SSH URL来克隆GitHub上的仓库了。在GitHub仓库页面上，点击“Code”按钮，然后选择“SSH”选项来复制SSH URL。然后，使用`git clone`命令和该URL来克隆仓库。

```bash
bash复制代码

git clone git@github.com:username/repository.git
```

将`username/repository.git`替换为你的GitHub用户名和仓库名。