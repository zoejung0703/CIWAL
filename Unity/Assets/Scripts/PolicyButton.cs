using UnityEngine;
using UnityEngine.UI;

public class PolicyButton : MonoBehaviour
{
    public string policyId;
    public int turnId;
    public Text buttonText;

    public void OnClick()
    {
        FindObjectOfType<GameManager>().ChoosePolicy(turnId, policyId);
    }
}
