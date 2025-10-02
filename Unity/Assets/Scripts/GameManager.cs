using UnityEngine;
using Newtonsoft.Json.Linq;

public class GameManager : MonoBehaviour
{
    private JObject gameState;
    private JObject choices = new JObject();

    public Transform policyButtonContainer;
    public GameObject policyButtonPrefab;
    public MetricBar gdpBar, happinessBar, freedomBar, equalityBar, sustainabilityBar;

    void Start()
    {
        LoadTurn(1); // start at first turn
    }

    public void ChoosePolicy(int turnId, string policyId)
    {
        choices[turnId.ToString()] = policyId;
        string resultJson = PythonBridge.RunPython(choices.ToString());
        JArray history = JArray.Parse(resultJson);

        JObject lastTurn = (JObject)history.Last;
        gameState = lastTurn;

        UpdateMetrics(lastTurn["metrics"] as JObject);

        if (lastTurn["ending"] != null)
        {
            ShowEnding(lastTurn);
        }
        else
        {
            LoadTurn((int)lastTurn["turn"] + 1);
        }
    }

    void LoadTurn(int turnId)
    {
        // Load from Resources/policy_data.json
        TextAsset jsonFile = Resources.Load<TextAsset>("policy_data");
        JObject data = JObject.Parse(jsonFile.text);
        JObject turn = (JObject)data["turns"].First(t => (int)t["turn_id"] == turnId);

        // Clear old buttons
        foreach (Transform child in policyButtonContainer) Destroy(child.gameObject);

        // Create buttons for policies
        foreach (JObject p in turn["policies"])
        {
            GameObject btnObj = Instantiate(policyButtonPrefab, policyButtonContainer);
            PolicyButton btn = btnObj.GetComponent<PolicyButton>();
            btn.policyId = p["id"].ToString();
            btn.turnId = turnId;
            btn.buttonText.text = p["name"].ToString();
        }

        // TODO: Change background to match era
        Debug.Log($"Era: {turn["era"]}");
    }

    void UpdateMetrics(JObject metrics)
    {
        gdpBar.SetValue((int)metrics["gdp"]);
        happinessBar.SetValue((int)metrics["happiness"]);
        freedomBar.SetValue((int)metrics["freedom"]);
        equalityBar.SetValue((int)metrics["equality"]);
        sustainabilityBar.SetValue((int)metrics["sustainability"]);
    }

    void ShowEnding(JObject turn)
    {
        Debug.Log("Game Over: " + turn["ending"]);
        // TODO: Show ending panel + orientation analysis
    }
}
