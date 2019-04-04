using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;
using System.Diagnostics;
using Flight;
using UnityEngine.SceneManagement;

namespace Flight
{

    public class FlyPlane : MonoBehaviour
    {
        public float speed;
        private bool enteredOne;
        private int inc;
        public Rigidbody rb;
        private float t;
        private List<double> xVel;
        private List<double> yVel;
        private List<double> zVel;
        private List<double> pitch;
        private List<double> roll;
        private List<double> yaw;

        Vector3 startingPos;
        Vector3 startingAngle;
        float travelTime;

        void Start()
        {

            inc = 0;
            enteredOne = false;
            Flight.PythonCalls check = new PythonCalls();
            check.callPython();
            xVel = check.xVelocity;
            yVel = check.yVelocity;
            zVel = check.zVelocity;
            pitch = check.pitch;
            roll = check.roll;
            yaw = check.yaw;


            travelTime = 0.025f;
            t = 0.0f;
            startingPos = new Vector3(48.65f, 26.2f, 78.66f);
            startingAngle = new Vector3(-90f, 0f, 0f);
          
        }

        // Update is called once per frame
        void FixedUpdate()
        {

            t += Time.deltaTime;
            if (t < 0.04f && enteredOne == false)
            {
                Vector3 Pos1 = startingPos + new Vector3((float)yVel[inc], (float)zVel[inc], (float)xVel[inc]);
                Vector3 Pos2 = startingPos + new Vector3((float)yVel[inc+1], (float)zVel[inc+1], (float)xVel[inc+1]);

                Vector3 Angle1 = startingAngle + new Vector3((float)pitch[inc], (float)yaw[inc] , (float)roll[inc]) * (float)(180 / Math.PI);
                Vector3 Angle2 = startingAngle + new Vector3((float)pitch[inc+1] , (float)yaw[inc+1] , (float)roll[inc+1] ) * (float)(180 / Math.PI);

                transform.position = Vector3.Lerp(Pos1 , Pos2, 0.5f);
                transform.eulerAngles = Vector3.Lerp(Angle1, Angle2, 0.5f);
                inc++;
                //UnityEngine.Debug.Log(t);
            }
            if(t > 0.04f)
            {
                enteredOne = false;
                t = 0;
            }


            //t = t + Time.deltaTime;
            //if (t < 0.025f && enteredOne == false)
            //{
              //  rb.velocity = new Vector3((float)yVel[inc], (float)zVel[inc], (float)xVel[inc]/);
                //rb.angularVelocity = new Vector3((float)pitch[inc], (float)yaw[inc], (float)roll[inc]);
                //inc++;
                //enteredOne = true;
                //UnityEngine.Debug.Log(xVel[inc]);
                //UnityEngine.Debug.Log(zVel[inc]);
                //UnityEngine.Debug.Log(t);
            //}

            //if (t > 0.025f)
            //{
              //  enteredOne = false;
                //t = 0;
            //}
        }
    }
   
}