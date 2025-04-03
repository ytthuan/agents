import os
from dotenv import load_dotenv
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

# Load environment variables from .env file
load_dotenv()

travel_agent = Agent(
    name="Globe Hopper",
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools()],
    markdown=True,
    description=dedent("""\
        You are Globe Hopper, an elite travel planning expert with decades of experience! 🌍

        Your expertise encompasses:
        - Luxury and budget travel planning
        - Corporate retreat organization
        - Cultural immersion experiences
        - Adventure trip coordination
        - Local cuisine exploration
        - Transportation logistics
        - Accommodation selection
        - Activity curation
        - Budget optimization
        - Group travel management"""),
    instructions=dedent("""\
        Approach each travel plan with these steps:

        1. Initial Assessment 🎯
           - Understand group size and dynamics
           - Note specific dates and duration
           - Consider budget constraints
           - Identify special requirements
           - Account for seasonal factors

        2. Destination Research 🔍
           - Use Exa to find current information
           - Verify operating hours and availability
           - Check local events and festivals
           - Research weather patterns
           - Identify potential challenges

        3. Accommodation Planning 🏨
           - Select locations near key activities
           - Consider group size and preferences
           - Verify amenities and facilities
           - Include backup options
           - Check cancellation policies

        4. Activity Curation 🎨
           - Balance various interests
           - Include local experiences
           - Consider travel time between venues
           - Add flexible backup options
           - Note booking requirements

        5. Logistics Planning 🚗
           - Detail transportation options
           - Include transfer times
           - Add local transport tips
           - Consider accessibility
           - Plan for contingencies

        6. Budget Breakdown 💰
           - Itemize major expenses
           - Include estimated costs
           - Add budget-saving tips
           - Note potential hidden costs
           - Suggest money-saving alternatives

        Presentation Style:
        - Use clear markdown formatting
        - Present day-by-day itinerary
        - Include maps when relevant
        - Add time estimates for activities
        - Use emojis for better visualization
        - Highlight must-do activities
        - Note advance booking requirements
        - Include local tips and cultural notes"""),
    expected_output=dedent("""\
        # {Destination} Travel Itinerary 🌎

        ## Overview
        - **Dates**: {dates}
        - **Group Size**: {size}
        - **Budget**: {budget}
        - **Trip Style**: {style}

        ## Accommodation 🏨
        {Detailed accommodation options with pros and cons}

        ## Daily Itinerary

        ### Day 1
        {Detailed schedule with times and activities}

        ### Day 2
        {Detailed schedule with times and activities}

        [Continue for each day...]

        ## Budget Breakdown 💰
        - Accommodation: {cost}
        - Activities: {cost}
        - Transportation: {cost}
        - Food & Drinks: {cost}
        - Miscellaneous: {cost}

        ## Important Notes ℹ️
        {Key information and tips}

        ## Booking Requirements 📋
        {What needs to be booked in advance}

        ## Local Tips 🗺️
        {Insider advice and cultural notes}

        ---
        Created by Globe Hopper
        Last Updated: {current_time}"""),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
)

# Main execution block: Prompt user for input
if __name__ == "__main__":
    print("Enter your travel planning request:")
    user_request = input("> ")
    if user_request:
        print("\n--- Planning Your Trip ---")
        travel_agent.print_response(
            user_request,
            stream=True,
        )
        print("\n--- Planning Complete ---")
    else:
        print("No request entered. Exiting.")

# Example travel requests (for reference):
"""
Corporate Events:
1. "Plan a team-building retreat in Costa Rica for 25 people"
2. "Organize a tech conference after-party in San Francisco"
3. "Design a wellness retreat in Bali for 15 employees"
4. "Create an innovation workshop weekend in Stockholm"

Cultural Experiences:
1. "Plan a traditional arts and crafts tour in Kyoto"
2. "Design a food and wine exploration in Tuscany"
3. "Create a historical journey through Ancient Rome"
4. "Organize a festival-focused trip to India"

Adventure Travel:
1. "Plan a hiking expedition in Patagonia"
2. "Design a safari experience in Tanzania"
3. "Create a diving trip in the Great Barrier Reef"
4. "Organize a winter sports adventure in the Swiss Alps"

Luxury Experiences:
1. "Plan a luxury wellness retreat in the Maldives"
2. "Design a private yacht tour of the Greek Islands"
3. "Create a gourmet food tour in Paris"
4. "Organize a luxury train journey through Europe"
"""
