<h1>Verkettete Liste</h1>

<h1>Zweck des Programmes</h1>

Diese Programm dient dazu die Verkettete Liste und die Doppelvekettete Liste besser zu verstehen. Auch der Vergleich zu einer ArrayList (in diesem Programm eine Python) liest wird deutlich. In diesem Programm findet man eine Reihen an Methoden die auf die Doppelverkettete Liste angepasst wurden.

<h1>Ausführen des Programms</h1>

Das Programm wurde in der entwicklungsumgebung VS-Code geschrieben sollte aber auch in jeder anderen Entwicklungsumgebung die Python unterstützt ausführbar sein. Das einzige das benötigt wird ist eine Aktuelle Python Version für die GUI.
Die verwendete Version ist 3.9.7.

<h1>Ablauf Programm ohne GUI</h1>
Das Programm startet und es wird eine Liste mit 10000 verschiedenen Werte imm Zahlenbereich von 0 bis 700000 erzeugt. Diese Liste wird in eine Doppelverkettete Liste und eine Arrayliste eingefügt. Die Zeit zum EInfügen wird gemessen und ausgegeben. Weiteres werden beide Listen zuerst aufsteigend sortiert und danach absteigen sortiert. Hier wird ebenfalls wieder die Zeit gemessen. Die gemessene Zeit wird ebenfalls in der Konsole ausgegeben.

<h1>Ablauf mit GUI:</h1>
Die Anzahl der erzeugten Zahlen muss eingegeben werden. Ab diesem Zeitpunkt läuft das Programm wieder gleich ab. Die Zeitmessungen werden auf dem Bildschirm ausgegeben.

![img_img](https://github.com/NoxusDarius/Liste/blob/master/Doppel/Bilder/gui.png)

Das Sortieren benötigt ungefähr 5 Sekunden für die ArrayList (Aufsteigend)
Das Sortieren benötigt ungefähr 10 Sekunden für die Verkettete Liste (Aufsteigend)
Das Absteigende Sortieren benötigt bei beiden Verfahren ungefähr doppelt so lange, da die Liste zuvor schon aufsteigend sortiert worden ist. Das bedeutet es ist der WOrst-Case um absteigend zu sortieren.

<h1>Aufwandsklassen</h1>
<table>
  <thead>
    <tr>
      <th>Methode</th>
       <th>Aufwandsklasse doppelt-verkettete Liste</th>
       <th>Aufwandsklasse Arraylist</th>
    </tr>
  </thead>
    <tr>
      <td>deleteAfter()</td>
      <td>n</td>
      <td>n</td>
  </tr>
   <tr>
      <td>deleteBefore()</td>
      <td>n</td>
      <td>n</td>
  </tr>
   <tr>
      <td>insertAfter()</td>
      <td>n</td>
      <td>n+1</td>
  </tr>
   <tr>
      <td>insertBefore()</td>
      <td>n</td>
      <td>n+1</td>
  </tr>
   <tr>
      <td>returnLength()</td>
      <td>n</td>
      <td>n</td>
  </tr>
   <tr>
      <td>sortASC()</td>
      <td>n^2</td>
      <td>n^2</td>
  </tr>
   <tr>
      <td>sortDESC()</td>
      <td>n^2</td>
      <td>n^2</td>
  </tr>
  <tr>
      <td>findbyIndex()</td>
      <td>n</td>
      <td>n</td>
  </tr>
  <tr>
      <td>findbyObjective()</td>
      <td>n</td>
      <td>n</td>
  </tr>
  </tbody>
  </table>
  
  
    

