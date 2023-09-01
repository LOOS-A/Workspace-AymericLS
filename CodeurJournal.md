# Journal personnel

Voici mon journal personnel de développeur dans lequel je place toutes mes petites astuces et résolutions de problèmes auquels j'ai pu être confronté. La structure des éléments remontés dans ce document étant importante je rappelle la façon de les ajouter.

**Date - Titre - Description - Mots clés - Solution**

- Les **mots clés** permettront de lister tous les éléments à retenir concernant l'élément du journal ajouté. Cela peut par exemple contenir le langage, la technologie, le type d'enregistrement etc. 
- La **solution** pourra tout aussi bien décrire la façon de résoudre le problème tout en essayant de tirer une réflexion sur le sujet problématique. Pourquoi ce problème est-il apparu ? Pourquoi le résoudre de telle ou telle manière etc.

## Liste des enregistrements

- 03/07/2023 - Could not load assembly - Lors de l'éxecution d'une application web, erreur à l'exécution: "Could not load file or assembly" provenant de l'analyse d'une DLL emballée - EID; ATEL; Assembly; .NET; DLL - Un paquet ATEL n'a pas forcément de tous les pré-requis lors de la compilation. En revanche, lors de l'exécution de l'application, certaines DLL ont besoin d'être présentes dans le dossier bin de l'application. Dans ce cas là, il faut bien vérifier que la DLL a bien été embarqué lors de la configuration du paquet en tant que paquet emaballé et non seulement en tant que pré-requis.
- 06/07/2023 - Contenu des DLL .NET inconnu - Sans avoir le code des DLL, comment connaître leur contenu tant en terme de code source que de références - EID; DLL; ILSpy; Références - L'outil ILSpy est un outil logiciel permettant de décompiler des DLL (par simple ouverture ou Drag and Drop). La décompilation permet de connaître le code source mais aussi les DLL référencées dans ce projet. Cet outil est pratique dans le contexte client car il permet d'éviter de constamment importer les projets sur son poste et de demander les droits adéquats.
- 10/07/2023 - Modifier le comportement du bouton retour sur un fragment d'une activité avec Navigation Drawer. Application avec une seule activité. - Sur une application avec une seule activité (Login au lancement puis Navigation Drawer) le clique sur le bouton retour sur un fragment de ce Navigation Drawer revient sur le fragment de Login - Android; Menu; Kotlin; Navigation - Pour modifier le comportement du bouton retour, il faut surcharger la méthode onBackPressed de l'activité principale. En revanche il ne faut pas oublier de surcharger la méthode onOptionsItemSelected wui permet en fait d'ouvrir et de fermer le menu de type Navigation Drawer.
```kotlin
override fun onBackPressed() {
  when(getCurrentFragment()){
    ActualFragment.Fragment1 -> {
      //Do something here
    }
    ActualFragment.Fragment2 -> {
      //Do something here
    }
    ActualFragment.FragmentAjoute -> {
      //Do something else here
    }
    else -> {
      super.onBackPressed()
    }
  }
}
override fun onOptionsItemSelected(item: MenuItem):Boolean {
        return when(item.itemId){
            R.id.item_1_menu -> {
                when(getCurrentFragment()){
                    ActualFragment.Fragment1, ActualFragment.Fragment2, ActualFragment.FragmentAjoute -> {
                        //Do something else here
                    }
                    else -> {
                        //Let's finish this activity
                        this.finishAffinity()
                    }
                }
                return true
            }
            //Following menu item represents the navigation drawer button
            android.R.id.home ->{
                when(getCurrentFragment()){
                    ActualFragment.Fragment1 -> {
                        //Do something else here
                    }
                    ActualFragment.Fragment1 -> {
                        //Do something else here
                    }
                    else -> {
                        onBackPressed()
                        return true
                    }
                }
            }
            else -> {
                super.onOptionsItemSelected(item)
            }
        }
    }

```
- 01/09/2023 - Project file must include the .net framework assembly windowsbase - Lors de la compilation d'une application de type .NET avec des fichiers sources utilisés pour l'affichage de messages d'erreurs, il peut arriver cette erreur. - .NET; DLL; Devbooster; Microsoft; Visual Studio - Il faut s'assurer en fait que le fichier XML/XAML permettant d'afficher les messages d'erreurs soit défini avec un "Build Action" de type "Embeded Resource" et non autre chose. La modification est effective immédiatement. Pas besoin de relancer Visual Studio.
