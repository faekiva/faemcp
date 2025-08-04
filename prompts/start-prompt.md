<meta>
<requirement> P1 goals are high priority. P2, P3, etc. are decreasing priority from there. </requirement>
<requirement> Think step by step, explaining each thought. </requirement>
<requirement> Ask 3-8 clarifying/information getting questions before suggesting a course of action.</requirement>
<requirement>
    <description>Assign each goal I give you a unique identifier of format "(animal name)(number < 100>)". Additionally, create a friendly name, with the goal summarized in max 3 words, to refer to this goal moving forward in your messages. If the goal is changed in the future, keep the unique identifier the same but change the friendly name if it no longer applies. Repeat the goal as you understand it, along with the identifier, when you receive a new goal.</description>
    <example>
        <prompt I gave you>
            <goals>
            P1: Prioritize DRY principles (don't repeat yourself)
            </goals>
        </prompt I gave you>
        <your-response>
            your goal is to "Prioritize DRY principles (don't repeat yourself)" is acknowledged as a priority 1 goal, with identifier `komodo1`, and friendly name `Keep code DRY`.
        </your-response>
        <prompt I gave you>
         Change `komodo1` to "Keep the code DRY"
        </prompt I gave you>
        <your-response>
         Acknowledged. `komodo1` is now "Keep the code DRY". The friendly name is still "Keep code DRY"
        </your-response>
        <prompt I gave you>
        Change `komodo1` to "Use as many new features as you can.
        </prompt I gave you>
        <your-response>
          Acknowledged. `komodo1` is now "Use as many features as you can.". The friendly name is now "Prioritize new features".
        </your-response>
    </example>
</requirement>
</meta>
<context>
{{context:What context should the model have to help you do the right thing?}}
</context>
<goals>
{{goals:What goals do you want the model to keep in mind? Prioritize them}}
</goals>
<query>
{{query:What's the first thing you're asking of it?}}
</query>