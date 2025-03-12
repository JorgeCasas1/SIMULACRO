# EXAMEN DE ED 1DAM
Aquí iré subiendo todos los datos relacionados con el examen de _Entornos De Desarrollo_.

1. [Python](#python)
    - Bucles
    - Listas
    - For
2. [Commits](#commits)
3. [NO SE TE VAYA A OLVIDAR](#olvidar)
4. [Espero que sigas atento](#atento)
5. [QUIERO ASEGURARME DE QUE NO TENGO COMMITS](#asegurar)
6. [Enlaces](#enlace)
7. [MAÑANA GANA EL MADRID](#madrid)

## 1. Python <div id="python"></div>
| Lista | Bucles | Funciones |
|-------|--------|----------|
| _[]_  | _for_  | _def_    |

>No fallará el clásico...

```python
print("Hola Mundo")
```

## 2. Commits <div id="commits"></div>

> Antes de nada. Como no hagas _git clone _"url de tu repositorio"_ estas jodido.

> Estos nos sirven para ir guardando todos los cambios que estamos haciendo en los archivos que vayamos modificando.

> Al meterte en Visual _RECUERDA_ que tienes que darle a _NEW TERMINAL_ y cuando se inicie. Introducir **git init** para empezar a hacer _COSITAS_....

```
git branch-> nos dice en la rama que nos encontramos.

git branch nueva rama-> es el nombre que le daremos, en este caso "nueva rama".

git checkout "nombre"-> nos llevará a la nueva rama creada.
```

## 3. NO SE TE HA DE OLVIDAR... <div id="olvidar"></div>

***Hacer commits cada _X_ _tiempo_, no vaya a ser que no mandes nada y suspendas el examen.***

- [x] Siempre haz el commit
- [ ] No se te ha de olvidar

¿Ahora que lo dices? Haré un **COMMIT**.

> ¡Asegúrate de que no te queden!

```
[main fb628ea] Otro commit para refrescar
 1 file changed, 18 insertions(+), 2 deletions(-)

C:\Users\Usuario\Desktop\SIMULACRO ED\EXAMEN>git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Vamos a enviarlo al origen con _git push origin main_

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 634 bytes | 11.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/JorgeCasas1/EXAMEN.git
   9ac74f0..fb628ea  main -> main
```

- [x] Si te sale ese mensaje, lo has realizado correctamente y el documento _.md_ aparecerá actualizado en tu repositorio.

## 4. ESPERO QUE SIGAS ATENTO... <div id="atento"></div>

`Entornos parecía fácil`, pero como no te mires el temario puedes irte al _"HOYO"_.

## 5. QUIERO ASEGURARME DE QUE NO TENGO COMMITS <div id="asegurar"></div>
Es sencillo, le damos a _git status_

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

> Mal asunto, no se ha guardado...

Vamos a guardarlo aplicando `git add .`.
Significa guardar **TODO**.

```
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```

_¡GENIAL, SE HA MODIFICADO!_

Toca hacerle la fotito...
```
C:\Users\Usuario\Desktop\SIMULACRO ED\EXAMEN>git commit -m "Actualización 3"
[main f72ce4a] Actualización 3
 1 file changed, 64 insertions(+), 4 deletions(-)
```
_¡GENIAL, NO TENEMOS QUE HACER POR AHORA MÁS COMMITS!_

```
C:\Users\Usuario\Desktop\SIMULACRO ED\EXAMEN>git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

> ¡QUE NO SE OLVIDE EL _git push origin main_!

## 6. Enlaces <div id="enlace"></div>

No creo que meta enlaces, pero bueno, si te aburres puedes meterte en el **Marca** un rato. Toma, te dejo el enlace: [enlace al Marca](https://www.marca.com/).

## 7. MAÑANA GANA EL MADRID <div id="madrid"></div>
![FOTO](https://www.bing.com/images/search?q=madrid%20foto&FORM=IQFRBA&id=FE9329E0236E97146E620CB5D25BC4C583314527)

> _PD: No aparece fotografía porque no la he metido en la carpeta._

_LOS CODIGOS DE PYTHON TOCA BUSCARSE LA VIDA_



