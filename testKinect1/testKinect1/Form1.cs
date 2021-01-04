using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using Microsoft.Kinect;

namespace testKinect1
{
    public partial class Form1 : Form
    {
        private KinectSensor sensor;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {


            try
            {
                sensor = KinectSensor.KinectSensors[0];
                sensor.Start();
                MessageBox.Show("Kinect Démarrée !");

                sensor.SkeletonStream.Enable();
                sensor.SkeletonFrameReady += SensorSkeletonFrameReady;


            }
            catch
            {
                MessageBox.Show("Pas de kinect Détectée !");
                Application.Exit();
            }

        }


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

                        lblX.Text = rightX.ToString();
                        lblY.Text = rightY.ToString();
                        lblZ.Text = rightZ.ToString();
                    }
                }
            }

        }
    }
}
