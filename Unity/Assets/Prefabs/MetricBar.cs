using UnityEngine;
using UnityEngine.UI;

public class MetricBar : MonoBehaviour
{
    public Text label;
    public Image fill;

    public void SetValue(int value)
    {
        fill.fillAmount = Mathf.Clamp01(value / 100f);
    }
}
