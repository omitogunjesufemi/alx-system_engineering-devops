0-iam-betty: This switches the current user to the user betty

1-who_am_i: This prints the effective username of the current user.

2-groups: This prints all the groups the current user is part of.

3-new_owner: This changes the owner of the file hello to the user betty.

4-empty: This creates an empty file called hello.

5-execute: This adds execute permission to the owner of the file hello.

6-multiple_permissions: This adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody: This adds execution permission to the owner, the group owner and the other users, to the file hello.

8-James_Bond: This sets the permission to the file hello as - Owner: no permission at all - Group: no permission at all - Other users: all the permissions.

9-John_Doe: This sets the mode of the file hello to -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

10-mirror_permissions: This sets the mode of the file hello the same as olleh’s mode.

11-directories_permissions: This adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

12-directory_permissions: This creates a directory called my_dir with permissions 751 in the working directory.

13-change_group: This changes the group owner to school for the file hello

100-change_owner_and_group: This changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

101-symbolic_link_permissions: This changes the owner and the group owner of _hello to vincent and staff respectively.

102-if_only: This changes the owner of the file hello to betty only if it is owned by the user guillaume.

103-Star_Wars: This play the StarWars IV episode in the terminal.
