using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class heightFromMarker : MonoBehaviour
{
    // The height to the marker. Public for other scripts to access.
    [HideInInspector]
    public float heightDifference;

    // The height to the floor. Public for other scripts to access.
    [HideInInspector]
    public float heightDifferenceToFloor;

    public Transform cameraTransform;
    public Transform targetTransform;


    // Update is called once per frame
    void Update()
    {
        heightDifference = Vector3.Distance(targetTransform.position, new Vector3(targetTransform.position.x, cameraTransform.position.y, targetTransform.position.z));
        Debug.Log(heightDifference);
    }
}
