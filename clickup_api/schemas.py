from typing import Optional, List, Any

from pydantic import BaseModel, ValidationError, validator, Field, field_validator

import json

from clickup_api import client


class Priority(BaseModel):
    priority: Optional[Any] = None
    color: Optional[str]


class Status(BaseModel):
    status: Optional[str] = None
    color: Optional[str] = None

    hide_label: Optional[bool] = None


class StatusElement(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None

    orderindex: Optional[int] = None
    color: Optional[str] = None

    type: Optional[str] = None


class Asssignee(BaseModel):
    id: Optional[int] = None
    color: Optional[str] = None
    username: Optional[str] = None
    initials: Optional[str] = None

    profilePicture: Optional[str] = None


class ListFolder(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

    hidden: Optional[bool] = None

    access: Optional[bool]


class SingleList(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    deleted: Optional[bool] = None

    archived: Optional[bool] = None

    orderindex: Optional[int] = None

    override_statuses: Optional[bool] = None

    priority: Optional[Priority] = None

    assignee: Optional[Asssignee] = None
    due_date: Optional[str] = None
    start_date: Optional[str] = None

    folder: Optional[ListFolder] = None

    space: Optional[ListFolder] = None

    statuses: Optional[List[StatusElement]] = None

    inbound_address: Optional[str] = None

    permission_level: Optional[str] = None

    content: Optional[str] = None

    status: Optional[Status] = None

    task_count: Optional[int] = None

    start_date_time: Optional[str] = None

    due_date_time: Optional[bool] = None

    # return a single list

    def build_list(self):
        return SingleList(**self)


class AllLists(BaseModel):
    lists: List[SingleList] = None

    # return a list of lists

    def build_lists(self):
        return AllLists(**self)


class ChecklistItem(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    orderindex: Optional[str] = None

    assignee: Optional[Asssignee]


class Checklist(BaseModel):
    id: Optional[str]

    task_id: Optional[str] = None
    name: Optional[str] = None

    orderindex: Optional[int] = None

    resolved: Optional[int] = None

    unresolved: Optional[int] = None

    items: List[ChecklistItem] = None

    def add_item(self, client_instance, name: str, assignee: str = None):
        return client_instance.create_checklist_item(
            self.id, name=name, assignee=assignee
        )


class Checklists(BaseModel):
    checklist: Checklist

    def build_checklist(self):
        final_checklist = Checklists(**self)

        return final_checklist.checklist


class Attachment(BaseModel):
    id: Optional[str]

    version: Optional[int]
    date: Optional[str]
    title: Optional[str]

    extension: Optional[str]

    thumbnail_small: Optional[str]

    thumbnail_large: Optional[str]
    url: Optional[str]

    def build_attachment(self):
        return Attachment(**self)


class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    initials: Optional[str] = None
    email: Optional[str] = None
    color: Optional[str] = None

    profilePicture: Optional[str] = None

    initials: Optional[str] = None

    role: Optional[int] = None

    custom_role: Optional[None] = None

    last_active: Optional[str] = None

    date_joined: Optional[str] = None

    date_invited: Optional[str] = None


class AssignedBy(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    initials: Optional[str] = None
    email: Optional[str] = None
    color: Optional[str] = None
    profile_picture: Optional[str] = None


class CommentComment(BaseModel):
    text: Optional[str] = None


class Comment(BaseModel):
    id: Optional[int] = None

    comment: List[CommentComment] = None

    comment_text: Optional[str] = None

    user: Optional[AssignedBy] = None

    resolved: Optional[bool] = None

    assignee: Optional[AssignedBy] = None

    assigned_by: Optional[AssignedBy] = None

    reactions: List[Any] = None
    date: Optional[int] = None
    hist_id: Optional[str] = None

    def build_comment(self):
        return Comment(**self)


class Comments(BaseModel):
    comments: List[Comment] = None

    def __iter__(self):
        return iter(self.comments)

    def build_comments(self):
        return Comments(**self)


class Creator(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    color: Optional[str] = None
    profile_picture: Optional[str] = None


class Option(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    color: Optional[str] = None

    order_index: Optional[int] = None


class TypeConfig(BaseModel):
    default: Optional[int] = None

    placeholder: Optional[str] = None

    new_drop_down: Optional[bool] = None

    options: Optional[List[Option]] = None

    include_guests: Optional[bool] = None

    include_team_members: Optional[bool] = None


class CustomItems(BaseModel):
    enabled: Optional[bool] = None

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "enabled": True
            }
        }


class DueDates(BaseModel):
    enabled: Optional[bool] = None

    start_date: Optional[bool] = None

    remap_due_dates: Optional[bool] = None

    remap_closed_due_date: Optional[bool] = None


class CustomField(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

    type: Optional[str] = None

    type_config: Optional[TypeConfig] = None
    date_created: Optional[str] = None

    hide_from_guests: Optional[bool] = None

    value: Optional[Any] = None

    required: Optional[bool] = None


class TimeTracking(BaseModel):
    enabled: Optional[bool] = False

    harvest: Optional[bool]= False

    rollup: Optional[bool] = False


class Sprints(BaseModel):
    enabled: Optional[bool] = False


class Points(BaseModel):
    enabled: Optional[bool] = False


class Zoom(BaseModel):
    enabled: Optional[bool] = False


class Milestones(BaseModel):
    enabled: Optional[bool] = False


class Emails(BaseModel):
    enabled: Optional[bool] = False


class MultipleAssignees(BaseModel):
    enabled: Optional[bool] = Field(default=None)


class TagsStatus(BaseModel):
    enabled: bool = False


class CustomFieldsStatus(BaseModel):
    enabled: Optional[bool] = False


class DependencyWarning(BaseModel):
    enabled: Optional[bool] = False


class TimeEstimateStatus(BaseModel):
    enabled: Optional[bool] = False


class RemapDependenciesStatus(BaseModel):
    enabled: Optional[bool] = False


class ChecklistsStatus(BaseModel):
    enabled: Optional[bool] = False


class PortfoliosStatus(BaseModel):
    enabled: Optional[bool] = False


class Features(BaseModel):
    due_dates: Optional[DueDates] = Field(None)

    multiple_assignees: Optional[MultipleAssignees] = Field( default_factory=MultipleAssignees)

    sprints: Optional[Sprints] = None

    start_date: Optional[bool] = False

    remap_due_dates: Optional[bool] = False

    remap_closed_due_date: Optional[bool] = False

    time_tracking: Optional[TimeTracking] = Field(default_factory=TimeTracking)

    tags: Optional[TagsStatus] = None

    time_estimates: Optional[TimeEstimateStatus] = None

    checklists: Optional[ChecklistsStatus] = None

    custom_fields: Optional[CustomFieldsStatus] = None

    remap_dependencies: Optional[RemapDependenciesStatus] = None

    dependency_warning: Optional[DependencyWarning] = None

    portfolios: Optional[PortfoliosStatus] = None

    points: Optional[Points] = None

    custom_items: Optional[CustomItems] = None

    zoom: Optional[Zoom] = None

    milestones: Optional[Milestones] = None

    emails: Optional[Emails] = None

    class Config:
        validate_assignment = True

    @field_validator("time_tracking", mode='before', check_fields=True)
    def set_tt(cls, time_tracking):
        return time_tracking or {"enabled": False}

    @field_validator("custom_fields", mode='before', check_fields=True)
    def set_cf(cls, custom_fields):
        return custom_fields or {"enabled": False}

    @field_validator("tags", mode='before', check_fields=True)
    def set_tags(cls, tags):
        return tags or {"enabled": False}

    @field_validator("multiple_assignees", mode='before', check_fields=True)
    def set_ma(cls, multiple_assignees):
        return multiple_assignees or {"enabled": False}

    @field_validator("checklists", mode='before', check_fields=True)
    def set_checklists(cls, checklists):
        return checklists or {"enabled": False}

    @field_validator("portfolios", mode='before', check_fields=True)
    def set_portfolios(cls, portfolios):
        return portfolios or {"enabled": False}


class SpaceFeatures(BaseModel):
    due_dates: Optional[bool] = False

    multiple_assignees: Optional[bool] = False

    start_date: Optional[bool] = False

    remap_due_dates: Optional[bool] = False

    remap_closed_due_date: Optional[bool] = False

    time_tracking: Optional[bool] = False

    tags: Optional[bool] = False

    time_estimates: Optional[bool] = False

    checklists: Optional[bool] = False

    custom_fields: Optional[bool] = False

    remap_dependencies: Optional[bool] = False

    dependency_warning: Optional[bool] = False

    portfolios: Optional[bool] = False

    points: Optional[bool] = False

    custom_items: Optional[bool] = False

    zoom: Optional[bool] = False

    milestones: Optional[bool] = False

    emails: Optional[bool] = False

    @property
    def all_features(self):
        return {
            "due_dates": {
                "enabled": self.due_dates,
                "start_date": self.start_date,
                "remap_due_dates": self.remap_due_dates,
                "remap_closed_due_date": self.remap_closed_due_date,
            },
            "time_tracking": {"enabled": self.time_tracking},
            "tags": {"enabled": self.tags},
            "time_estimates": {"enabled": self.time_estimates},
            "checklists": {"enabled": self.checklists},
            "custom_fields": {"enabled": self.custom_fields},
            "remap_dependencies": {"enabled": self.remap_dependencies},
            "dependency_warning": {"enabled": self.dependency_warning},
            "portfolios": {"enabled": self.portfolios},
            "milestones": {"enabled": self.milestones},
        }


class Space(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    access: Optional[bool] = None

    features: Optional[Features] = None

    multiple_assignees: Optional[bool] = None

    private: Optional[bool] = False

    statuses: Optional[List[Status]] = None

    archived: Optional[bool] = None

    def build_space(self):
        return Space(**self)


class Spaces(BaseModel):
    spaces: List[Space] = None

    def __iter__(self):
        return iter(self.spaces)

    def build_spaces(self):
        return Spaces(**self)


class Folder(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    orderindex: Optional[int] = None

    override_statuses: Optional[bool] = False

    hidden: Optional[bool] = False

    space: Optional[Space] = None

    task_count: Optional[int] = None

    lists: List[SingleList] = []

    def build_folder(self):
        return Folder(**self)

    def delete(self, client_instance):
        model = "folder/"

        deleted_folder_status = client_instance._delete_request(model, self.id)


class Folders(BaseModel):
    folders: List[Folder] = None

    def build_folders(self):
        return Folders(**self)


class Priority(BaseModel):
    id: Optional[int] = None

    priority: Any = None
    color: Optional[str] = None

    orderindex: Optional[str] = None


class Status(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    color: Optional[str] = None

    orderindex: Optional[int] = None

    type: str = None


class ClickupList(BaseModel):
    id: Optional[str] = None


# class Folder(BaseModel):

#     id: str = None


class Task(BaseModel):
    id: Optional[str] = None
    custom_id: Optional[str] = None
    name: Optional[str] = None

    text_content: Optional[str] = None
    description: Optional[str] = None

    status: Optional[Status] = None

    orderindex: Optional[str] = None
    date_created: Optional[str] = None
    date_updated: Optional[str] = None
    date_closed: Optional[str] = None

    creator: Optional[Creator] = None

    assignees: Optional[List[Asssignee]] = None

    task_checklists: Optional[List[Any]] = Field(None, alias="checklists")

    task_tags: Optional[List[Any]] = Field(None, alias="tags")
    parent: Optional[str] = None

    priority: Optional[Any] = None
    due_date: Optional[str] = None
    start_date: Optional[str] = None
    time_estimate: Optional[str] = None

    time_spent: Optional[int] = None

    custom_fields: Optional[List[CustomField]] = None
    list: Optional[ClickupList] = None

    folder: Optional[Folder] = None

    space: Optional[Folder] = None
    url: Optional[str] = ""

    def build_task(self):
        return Task(**self)

    def delete(self):
        client.ClickUpClient.delete_task(self, self.id)

    def upload_attachment(self, client_instance, file_path: str):
        return client_instance.upload_attachment(self.id, file_path)

    def update(
            self,
            client_instance,
            name: str = None,
            description: str = None,
            status: str = None,
            priority: Any = None,
            time_estimate: int = None,
            archived: bool = None,
            add_assignees: List[str] = None,
            remove_assignees: List[int] = None,
    ):
        return client_instance.update_task(
            self.id,
            name,
            description,
            status,
            priority,
            time_estimate,
            archived,
            add_assignees,
            remove_assignees,
        )

    def add_comment(
            self,
            client_instance,
            comment_text: str,
            assignee: str = None,
            notify_all: bool = True,
    ):
        return client_instance.create_task_comment(
            self.id, comment_text, assignee, notify_all
        )

    def get_comments(self, client_instance):
        return client_instance.get_task_comments(self.id)


class Tasks(BaseModel):
    tasks: List[Task] = None

    def __iter__(self):
        return iter(self.tasks)

    def build_tasks(self):
        return Tasks(**self)


class User(BaseModel):
    id: Optional[int] = Field(default=None)
    username: Optional[str] = Field(default=None)
    initials: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    color: Optional[str] = Field(default=None)

    profilePicture: Optional[str] = Field(default=None)

    role: Optional[int] = Field(default=None)

    custom_role: Optional[None] = None

    last_active: Optional[str] = None

    date_joined: Optional[str] = None

    date_invited: Optional[str] = None


class InvitedBy(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    color: Optional[str] = None
    email: Optional[str] = None
    initials: Optional[str] = None
    profile_picture: Optional[None] = None


class Member(BaseModel):
    user: Optional[User] = None

    invited_by: Optional[InvitedBy] = None


class Members(BaseModel):
    members: List[User] = None

    def __iter__(self):
        return iter(self.members)

    def build_members(self):
        return Members(**self)


class Team(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    color: Optional[str] = Field(default=None)

    avatar: Optional[str] = Field(default=None)

    members: List[Member] = Field(default=None)


class Teams(BaseModel):
    teams: List[Team] = None

    def __iter__(self):
        return iter(self.teams)

    def build_teams(self):
        return Teams(**self)


class Goal(BaseModel):
    id: str = None
    name: str = None
    team_id: int = None
    date_created: str = None
    start_date: str = None
    due_date: str = None
    description: str = None

    private: bool = None

    archived: bool = None
    creator: int = None
    color: str = None

    pretty_id: int = None

    multiple_owners: bool = None
    folder_id: str = None

    members: List[User] = None

    owners: List[User] = None

    key_results: List[Any] = None
    percent_completed: int = None

    history: List[Any] = None

    pretty_url: str = None

    def build_goal(self):
        return Goal(**self)


class Goals(BaseModel):
    goal: Goal

    def build_goals(self):
        built_goal = Goals(**self)

        return built_goal.goal


class GoalsList(BaseModel):
    goals: List[Goal] = None
    folders: List[Folder] = None

    def __iter__(self):
        return iter(self.goals)

    def build_goals(self):
        return GoalsList(**self)


class Tag(BaseModel):
    name: str = None

    tag_fg: str = None

    tag_bg: str = None

    def build_tag(self):
        return Tag(**self)


class Tags(BaseModel):
    tags: List[Tag] = None

    def __iter__(self):
        return iter(self.tags)

    def build_tags(self):
        return Tags(**self)


class Shared(BaseModel):
    tasks: Optional[List[Tasks]]

    lists: Optional[List[SingleList]]

    folders: Optional[List[Folder]]

    def build_shared(self):
        return Shared(**self)

    def __iter__(self):
        return iter(self.shared)


class SharedHierarchy(BaseModel):
    shared: Shared

    def build_shared(self):
        return SharedHierarchy(**self)

    def __iter__(self):
        return iter(self.shared)


class TimeTrackingData(BaseModel):
    id: str = ""
    task: Task = None
    wid: str = ""
    user: User = None
    billable: bool = False
    start: str = ""
    end: str = ""
    duration: int = None
    description: str = ""
    tags: List[Tag] = None
    source: str = ""
    at: str = ""

    def build_data(self):
        return TimeTrackingData(**self)


class TimeTrackingDataList(BaseModel):
    data: List[TimeTrackingData] = None

    def build_data(self):
        return TimeTrackingDataList(**self)

    def __iter__(self):
        return iter(self.data)


class TimeTrackingDataSingle(BaseModel):
    data: TimeTrackingData = None

    def build_data(self):
        return TimeTrackingDataSingle(**self)

    def __iter__(self):
        return iter(self.data)