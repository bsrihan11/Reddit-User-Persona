from langchain_core.output_parsers import JsonOutputParser
from typing import List, Union, Literal
from pydantic import BaseModel, Field, HttpUrl


class FieldWithCitations(BaseModel):
    value: str = Field(default="", description="The main string value for this field")
    citations: List[HttpUrl] = Field(default_factory=list, description="List of URLs citing this value")


class FieldWithListValue(BaseModel):
    value: List[str] = Field(default_factory=list, description="List of extracted values")
    citations: List[HttpUrl] = Field(default_factory=list, description="List of URLs citing this list")


class PersonalityValue(BaseModel):
    key_tones: List[str] = Field(default_factory=list, description="Key tones like kind, sarcastic, analytical, helpful, etc.")
    energy: Union[Literal["Introvert", "Extrovert"], None] = Field(default=None, description='Energy orientation: "Introvert" or "Extrovert"')
    identity: Union[Literal["Assertive", "Turbulent"], None] = Field(default=None, description='Self-identity trait: "Assertive" or "Turbulent"')
    mind: Union[Literal["Observant", "Intuitive"], None] = Field(default=None, description='Thinking style: "Observant" or "Intuitive"')
    tactics: Union[Literal["Judging", "Prospecting"], None] = Field(default=None, description='Decision-making approach: "Judging" or "Prospecting"')
    nature: Union[Literal["Thinking", "Feeling"], None] = Field(default=None, description='Emotional nature: "Thinking" or "Feeling"')


class Personality(BaseModel):
    value: PersonalityValue = Field(default_factory=PersonalityValue, description="Detailed personality traits and preferences")
    citations: List[HttpUrl] = Field(default_factory=list, description="Sources for inferred personality")


class BehaviorItem(BaseModel):
    behavior: str = Field(default="", description="Label or name of the behavior/habit")
    description: str = Field(default="", description="Brief explanation of the behavior/habit with context")


class BehaviorAndHabits(BaseModel):
    value: List[BehaviorItem] = Field(default_factory=list, description="Inferred behaviors and personal habits with brief explanations")
    citations: List[HttpUrl] = Field(default_factory=list, description="Sources backing behavior inferences")


class UserPersona(BaseModel):
    username: str = Field(default="", description="The Reddit username")
    estimated_age_range: FieldWithCitations = Field(
        default_factory=FieldWithCitations,
        description="Estimated age range"
    )
    gender: FieldWithCitations = Field(
        default_factory=FieldWithCitations,
        description="Self-identified or strongly implied gender"
    )
    location: FieldWithCitations = Field(
        default_factory=FieldWithCitations,
        description="Mentioned or inferred location"
    )
    occupation_or_education: FieldWithCitations = Field(
        default_factory=FieldWithCitations,
        description="Occupation or education background (only if explicitly mentioned or strongly implied)"
    )
    personality: Personality = Field(
        default_factory=Personality,
        description="Summary of inferred personality traits with MBTI-like indicators"
    )
    hobbies_and_interests: FieldWithListValue = Field(
        default_factory=FieldWithListValue,
        description="User hobbies and interests"
    )
    behavior_and_habits: BehaviorAndHabits = Field(
        default_factory=BehaviorAndHabits,
        description="General User behaviors and habits"
    )
    most_active_subreddits: FieldWithListValue = Field(
        default_factory=FieldWithListValue,
        description="Subreddits where the user is most active"
    )
    quote_or_signature_style: FieldWithCitations = Field(
        default_factory=FieldWithCitations,
        description="Summarize the user's personality in one short motto"
    )


parser = JsonOutputParser(pydantic_object=UserPersona)
