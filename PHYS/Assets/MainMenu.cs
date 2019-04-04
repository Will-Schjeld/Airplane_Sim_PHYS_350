using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace Flight
{
    public class MainMenu : MonoBehaviour
    {
        public float speed;

        public void PlayGame()
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
        }

        public void AdjustSpeed(float newSpeed)
        {
            speed = newSpeed;
        }

    }
}

