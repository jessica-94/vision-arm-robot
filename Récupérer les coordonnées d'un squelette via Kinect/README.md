# Kinect Microsoft dans un projet Windows Form C# #

## Démarrer un projet Windows Form ##

Dans Visual Studio, démarrer un nouveau projet Windows Form appeler testKinect1.


- Pour utiliser la Kinect dans notre programme, nous devons lui inclure la référence à son SDK. Dans l'explorateur de solutions :
- Clic droit sur Références.
 - Ajouter une référence...
 - Sélectionner Extensions puis sélectionner Microsoft.Kinect
 ![Ajouter la référence Microsoft.Kinect ](http://silanus.fr/sin/wp-content/uploads/2017/02/Microsoft.Kinect.png)

Pour simplifier l'écriture du code faisant appel aux services de cette extension, nous allons ajouter l'espace de nom correspondant :

    using Microsoft.Kinect;

##  Vérifier la présence d'une Kinect ##

Cette vérification devrait être faite lors du chargement du formulaire :

- Double-clic sur le formulaire pour générer l’événement   private void Form1_Load(object sender, EventArgs e)
- Un peu plus haut dans le code, nous allons déclarer un objet de la classe KinectSensor :

    private KinectSensor sensor;

Il ne reste plus qu'à tester si une Kinect est bien connectée à l'ordinateur. Dans ce cas, on la démarre sinon, on affiche un message d'erreur et on quitte le programme :

    try
    {
       sensor = KinectSensor.KinectSensors[0];  //Une seule Kinect connectée
       sensor.Start();
       MessageBox.Show("Kinect Démarrée !");
    }
    catch
    {
       MessageBox.Show("Pas de kinect Détectée !");
       Application.Exit();
    }


## Obtenir les informations d'un squelette ##

La Kinect est capable de reconnaître les joueurs qui interagissent avec celle-ci. Le processus consiste à identifier le squelette du joueur qui sera fourni sous forme d'une collection de points 3D avec un index pour identifier le joueur (1 à 6).

Chaque squelette est composé de jointures :  **HipCenter, ShoulderCenter, Spine, Head, ShoulderLeft, ShoulderRight, ElbowLeft, ElbowRight, WristLeft, WristRight, HandLeft, HandRight, HipLeft, HipRight, KneeLeft, KneeRight, AnkleLeft, AnkleRight, FootLeft et FootRight**.

![Les jointures détectées](http://silanus.fr/sin/wp-content/uploads/2017/02/bodyparts.jpg)

L’événement permettant de récupérer les données reliées aux squelettes est `SkeletetonFrameReadyEventArgs`. Cet événement retourne un objet de type SkeletonFrame avec la méthode `OpenSkeletonFrame`.

Une fois la kinect démarrer, il faut activer la lecture des squelettes et créer le gestionnaire d'événement.

    MessageBox.Show("Kinect Démarrée !");
    sensor.SkeletonStream.Enable();
    sensor.SkeletonFrameReady += SensorSkeletonFrameReady; //gestionnaire d'événement appelé 30x par seconde !

Il ne reste plus qu'a écrire le gestionnaire de l'événement, par exemple pour suivre le déplacement de la main droite du squelette détecté :

    private void SensorSkeletonFrameReady(object sender, SkeletonFrameReadyEventArgs e)
    {
      Skeleton[] skeletons = new Skeleton[0];
    
      using (SkeletonFrame skeletonFrame = e.OpenSkeletonFrame())
      {
        if (skeletonFrame != null)
        {
          skeletons = new Skeleton[skeletonFrame.SkeletonArrayLength];
          skeletonFrame.CopySkeletonDataTo(skeletons);
        }
    
        foreach (Skeleton skeleton in skeletons)
        {
          if (skeleton.TrackingState == SkeletonTrackingState.Tracked)
          {
            Joint rightHand = skeleton.Joints[JointType.HandRight];
            float rightX = rightHand.Position.X;
            float rightY = rightHand.Position.Y;
            float rightZ = rightHand.Position.Z;
      
            lblX.Text = "X="+rightX.ToString();
            lblY.Text = "Y="+rightY.ToString();
            lblZ.Text = "Z="+rightZ.ToString();
          }
        }
      }
    }

![testKinect1](http://silanus.fr/sin/wp-content/uploads/2017/02/rightHand.png)