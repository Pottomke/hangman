def display_hangman(tries):
    stages = [  """

""",
"""



,%%%%%%%%,                                  ,%%%>
     %%o%%/%%%%%%                         ,%%%%%%%%%%>
    %%%%\%%%<%%%%%                       <%%%%%%%%%%%%%%%\
    %%>%%%/%%%%o%%                         <%%%%%/%%%\%%%>
    %%%%%o%%\%%//%                          s  <%%%%%%%%%>
    %\o%\%%/%o/%%'                         ő    ő   s   ő   s
     '%%\ `%/%%%'                        ő   ő   s    s   ő
       '%| |%|%'==%=\
         | |         O                   ő   s  ő   s   ő
         | |        (|)
         | |        / \               ő   s   ő  ő   s   ő   ő
         | |       
        /   \                            s  ő    s   ő   s  ő
 jgs^^^^^^^^^^^^^^^^^

 """,
"""


,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'==%=\
         | |        (O
         | |         |\
         | |         >>
         | |    
        /   \
 jgs^^^^^^^^^^^^^^^^^

""",
"""


 ,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'==%=\
         | |        (O
         | |         |\
         | |         >
         | |    
        /   \
 jgs^^^^^^^^^^^^^^^^^

 """,
"""


 ,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'==%=\
         | |        (O
         | |         |\
         | |         
         | |
        /   \
 jgs^^^^^^^^^^^^^^^^^

 """,
"""


 ,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'==%=\
         | |        (O
         | |         |
         | |         
         | |
        /   \
 jgs^^^^^^^^^^^^^^^^^

 """,
"""


 ,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'==%=\
         | |        (O
         | |         
         | |         
         | |  
        /   \
 jgs^^^^^^^^^^^^^^^^^

 """,
"""


 ,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'==%=\
         | |         O
         | |         
         | |         
         | |  
        /   \
 jgs^^^^^^^^^^^^^^^^^

 """,
"""


 ,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'==%=\
         | |        
         | |         
         | |         
         | |    
        /   \
 jgs^^^^^^^^^^^^^^^^^

 """,
"""

                                                      | | | |
 ,%%%%%%%%,                                         \*********/
     %%o%%/%%%%%%                                 \* ()   ()   */
    %%%%\%%%<%%%%%                               -*             *-
    %%>%%%/%%%%o%%                               -*   %     %   *-
    %%%%%o%%\%%//%                                /*   %%%%    *\
    %\o%\%%/%o/%%'                                  /*********\
     '%'%| |%|%'==%=\                                | | | | | 
         | |                       
         | |       \ O /
         | |         |          ÚJRATERVEZÉS 2.0
         | |        / \
        /   \     (%%%%%)
 jgs^^^^^^^^^^^^^^  | |

 """]